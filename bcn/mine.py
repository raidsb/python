# processing image data
import os

import nibabel as nib
from nilearn.image import resample_img
from nilearn.masking import apply_mask
import pickle
import dask.array as da
# processing csv data
import csv
from sklearn.preprocessing import MinMaxScaler
# processing binary
import numpy as np
from torch_geometric.utils import to_networkx
from scipy.spatial.distance import cdist
# Learning
import torch
from torch.utils.data import Dataset
from torch_geometric.data import Data as gdata
from torch_geometric.graphgym.loader import load_dataset
from sklearn.model_selection import train_test_split
import networkx as nx
from torch_geometric.nn import GCNConv, global_add_pool
from torch_geometric.data import DataLoader as gdataLoader

# plotting
import matplotlib.pyplot as plt
import math
import logging
import shutil
import datetime as dt

import nilearn
from nilearn import plotting
from nilearn import image

# -----------------------------------------------------------------
if os.path.isdir("C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\log"):
    shutil.rmtree("C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\log")
os.mkdir("C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\log")

logging.basicConfig(filename='C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\log\\log.log', encoding='utf-8', level=logging.INFO)
log_dir = "C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\log\\"

# Loading ABIDE_2_BNI
class ABIDE2_BNI():
    dataset_csv_file = "C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\ds\\abide2\\ABIDE_source_BNI\\ABIDEII-BNI_1.csv"
    image_dir = "C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\ds\\abide2\\ABIDE_source_BNI\\ABIDEII-BNI_1\\ABIDEII-BNI_1"
    atlas = "C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\ds\\AAL_Atlas_from_neurovault\\AAL.nii.gz"
    sessions = ["session_1"]
    image_scans = ["anat_1", "dti_1", "rest_1"]
    count_rows = 0
    csv_data_list = []
    img_path_list_anat = []
    AAL_Atlas_img_data = None
    AAL_Atlas_bin_data = None
    Graph_data_list = []
    plotting_img_slice_number = 190

    def __init__(self):
        self.load_atlas()
        self.load_ABIDE_2_bni()

    def load_atlas(self):
        # Load .nii file
        self.AAL_Atlas_img_data = nib.load(self.atlas)
        logging.info("Loading nii file of the Atlas")

        # convert loaded image into NumPy array
        self.AAL_Atlas_bin_data = self.AAL_Atlas_img_data.get_fdata()
        logging.info("Loading Atlas. Shape: " + str(self.AAL_Atlas_bin_data.shape))

    def load_ABIDE_2_bni(self):
        # Loading the csv file and construct the paths to images
        with open(self.dataset_csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            self.csv_data_list = [row for row in csv_reader]

            for d in self.csv_data_list:
                for session in self.sessions:
                    for a in self.image_scans:
                        image_path_column_name = "|".join([session, a])
                        image_path = "\\".join([self.image_dir, d["SUB_ID"], session, a, ".".join([a[:-2], "nii", "gz"])])
                        d[image_path_column_name] = image_path
                        if a == "anat_1":
                            self.img_path_list_anat.append(image_path)

    def print_rebuilt_csv(self):
        print(self.csv_data_list)

    def load_image(self, file_path, normalize=False):
        nii_image_data = nib.load(file_path)
        nii_bin_data_original = nii_image_data.get_fdata() # image is converted into NumPy arrays

        # Normalize values between [-1, 1]
        if normalize:
            scaler = MinMaxScaler()
            nii_bin_data_normalized = scaler.fit_transform(nii_bin_data_original.reshape(-1, 1)).reshape(nii_bin_data_original.shape)

        return nii_image_data, nii_bin_data_original, nii_bin_data_normalized

    def plot_image(self, image_data, slice):
        # print(image_data.shape)
        test = image_data[..., slice]
        plt.imshow(test)
        plt.show()

    def save_image(self, image_data, slice, filename):
        plt.imsave(filename, image_data[..., slice])

    def get_training_indexes(self):
        return 0, math.floor(len(self.csv_data_list) * 0.8)

    def get_validation_indexes(self):
        return math.floor(len(self.csv_data_list) * 0.8) + 1, len(self.csv_data_list) - 1

    def load_dataset(self):
        self.AAL_Atlas_bin_data[np.isin(self.AAL_Atlas_bin_data, 0, invert=True)] = 1

        # load exam data
        for i, file_path in enumerate(self.img_path_list_anat[:10]):
            # get the image data and the bin data
            nii_img_data, nii_bin_data_original, nii_bin_data_normalized = self.load_image(file_path, normalize=True)

            # Logging the loaded image
            # Logging original image
            logging.info("Loaded original image shape: " + str(nii_bin_data_original.shape))
            logging.info("Saving slice 190 of original image: " + file_path)
            save_file_name_original = log_dir + str(i) + "_original_" + file_path.replace("\\", "").replace(":", "").replace(".", "") + ".png"
            logging.info("Saving original image" + save_file_name_original)
            self.save_image(nii_bin_data_original, self.plotting_img_slice_number, save_file_name_original)
            logging.info("Loaded original image data values Min:" + str(np.min(nii_bin_data_original)) + "Max: " +
                         str(np.max(nii_bin_data_original)) + "unique: " + str(np.unique(nii_bin_data_original)))
            logging.info("")
            # Logging normalized image
            logging.info("Loaded normalized image shape: " + str(nii_bin_data_normalized.shape))
            logging.info("Saving slice 190 of loaded image: " + file_path)
            save_file_name_normalized = log_dir + str(i) + "_normalized_" + file_path.replace("\\", "").replace(":", "").replace(".", "") + ".png"
            logging.info("Saving normalized image" + save_file_name_normalized)
            self.save_image(nii_bin_data_normalized, self.plotting_img_slice_number, save_file_name_normalized)
            logging.info("Loaded normalized image data values Min:" + str(np.min(nii_bin_data_normalized)) + "Max: " +
                    str(np.max(nii_bin_data_normalized)) + "unique: " + str(np.unique(nii_bin_data_normalized)))
            logging.info("Normalized image data values Min: " + str(np.min(nii_bin_data_normalized)) + " Max: " +
                    str(np.max(nii_bin_data_normalized)) + " unique: " + str(
            np.unique(nii_bin_data_normalized)))

            # Resample AAL atlas to match the resolution of the images and convert to binary array
            aal_atlas_resampled_img = resample_img(nib.load(self.atlas), target_affine=nii_img_data.affine, target_shape=nii_bin_data_normalized.shape)
            aal_atlas_resampled_data = aal_atlas_resampled_img.get_fdata()

            # logging resampled AAL
            logging.info("Resampled Atlas: " + str(aal_atlas_resampled_data.shape))
            resampled_atlas_file_name = log_dir + str(i) + "_resampled_atlas_" + file_path.replace("\\", "").replace(":", "").replace(".", "") + ".png"
            self.save_image(aal_atlas_resampled_data, self.plotting_img_slice_number, resampled_atlas_file_name)

            # Normalize the AAL to [-1, 1]
            scaler = MinMaxScaler()
            aal_atlas_data_resampled_normalized = scaler.fit_transform(aal_atlas_resampled_data.reshape(-1, 1)).reshape(aal_atlas_resampled_data.shape)

            # logging resampled Atlas normalized
            logging.info("Resampled Atlas data values Min: " + str(np.min(aal_atlas_data_resampled_normalized)) + " Max: " + str(np.max(aal_atlas_data_resampled_normalized)) + "unique:" +
                  str(np.unique(aal_atlas_data_resampled_normalized)))

            # Masking image data with the Atlas
            # using the numpy
            masked_binary_image = np.multiply(nii_bin_data_normalized, aal_atlas_data_resampled_normalized)

            # Logging the masked bin img
            logging.info("Masked image shape: " + str(masked_binary_image.shape))
            masked_image_file_name = log_dir + str(i) + "_masked_img_" + file_path.replace("\\", "").replace(":",
                                    "").replace(".", "") + ".png"
            self.save_image(masked_binary_image, self.plotting_img_slice_number, masked_image_file_name)
            logging.info("Masked image data values Min: " + str(np.min(masked_binary_image)) + " Max: " + str(
                np.max(masked_binary_image)) + "unique:" +
                         str(np.unique(masked_binary_image)))

            masked_ni_img = nib.Nifti1Image(masked_binary_image, affine=np.eye(4))
            normalized_ni_img = nib.Nifti1Image(nii_bin_data_normalized, affine=np.eye(4))
            atlas_resampled_normalized_ni_img = nib.Nifti1Image(aal_atlas_data_resampled_normalized, affine=np.eye(4))
            nilearn.plotting.plot_img(normalized_ni_img)
            nilearn.plotting.show()
            nilearn.plotting.plot_img(atlas_resampled_normalized_ni_img)
            nilearn.plotting.show()
            nilearn.plotting.plot_img(masked_ni_img)
            nilearn.plotting.show()

            # unique_labels = np.unique(masked_binary_image)
            # print("unique labels: ", unique_labels)
            # #roi_mapping = {label: f'ROI_{label}' for label in unique_labels}

            # roi_labels = np.vectorize(roi_mapping.get)(masked_binary_image)
            # unique_rois = np.unique(roi_labels)
            # num_rois = len(unique_rois)
            # print(f"Number of grouped ROIs: {num_rois}")

            # nilearn_aal_atlas = nilearn.datasets.fetch_atlas_aal
            # print(nilearn_aal_atlas)
            # nilearn.plotting.plot_img(nilearn_aal_atlas)
            # nilearn.plotting.show()

            # Using nilear
            # masked_binary_image = apply_mask(nii_img_data, aal_atlas_resampled_img)




            # ########################################################### try0
            # Use this when the Atlas has already defined regions lables.
            # roi_nodes = [np.column_stack(np.where(roi)) for roi in masked_binary_image]
            # """
            # The results of this is list of tuples of this array([], shape=(0, 2), dtype=int64). number of tuples is 193 tuple.
            # array([[ 48, 137],
            #        [ 49, 147],
            #        [ 51, 140],
            #        [ 51, 160]], dtype=int64), the array for a slice having values. so (slice number, 51, 160) is a voxel.
            # """

            # Use this when you want the unique regions defined by the atlas.
            # unique_rois = np.unique(masked_binary_image) # Unique Rois or labels
            # print("nuber of nodes: ", len(unique_rois))

            # for label in unique_rois:
            #     # Extract all voxels corresponding to the current label
            #     region_voxels = np.where(masked_binary_image == label)
            #
            #     # Process or visualize the region as needed
            #     print(f"Region {label}: Voxel coordinates {region_voxels}")

            # Extract voxel coordinates for each unique region
            # roi_nodes = [np.column_stack(np.where(masked_binary_image == roi_value)) for roi_value in unique_rois]

            # Create a graph
            # G = nx.Graph()

            # # Add nodes to the graph
            # print("adding graph")
            # for idx, roi_coords in enumerate(roi_nodes):
            #     print("adding ", idx)
            #     G.add_node(idx, coords=roi_coords)
            #
            # # Add edges based on some measure (e.g., Euclidean distance between centroids)
            # for ic in range(len(roi_nodes)):
            #     for j in range(ic + 1, len(roi_nodes)):
            #         dist = np.linalg.norm(np.mean(roi_nodes[ic], axis=0) - np.mean(roi_nodes[j], axis=0))
            #         G.add_edge(ic, j, weight=dist)

            # show the graph
            # print(G)
            # pos = nx.spring_layout(G)  # You can use different layout algorithms
            # nx.draw_networkx(G, pos=pos, with_labels=False, node_size=10)
            # plt.show()

            # ########################################################### try1
            # threshold = 0.5
            # nodes = np.column_stack(np.where(masked_binary_image))
            # distances = cdist(nodes, nodes, 'euclidean')
            # threshold = 10  # Adjust this threshold based on your data
            # # edges = np.column_stack(np.where(distances < threshold))
            # G = nx.Graph()
            #
            # for ii, coord in enumerate(nodes):
            #     G.add_node(ii, pos=(coord[0], coord[1]))
            #
            # threshold_distance = 10  # Adjust this threshold as needed
            # for ti in range(len(nodes)):
            #     for j in range(ti + 1, len(nodes)):
            #         if distances[ti, j] < threshold_distance:
            #             G.add_edge(ti, j)

            # ############################################################ try2
            # flattened_image = masked_binary_image.reshape(masked_binary_image.shape[0], -1)
            # features = torch.from_numpy(flattened_image).float()
            # # for r in flattened_image:
            # #     print(r)
            # # calculate the Pearson Correlation
            # # correlation_matrix = np.corrcoef(masked_binary_image.flatten(), rowvar=False)
            # correlation_matrix = np.corrcoef(flattened_image, rowvar=True)
            # print('-------------> coefficient: ', correlation_matrix)
            #
            # G = nx.Graph()
            # num_features = features.shape[0]
            # for f in range(num_features):
            #     for j in range(f + 1, num_features):
            #         correlation_coefficient = correlation_matrix[f, j]
            #         if abs(correlation_coefficient) > threshold:
            #             G.add_edge(f, j, weight=correlation_coefficient)

            # ############################################################# try3
            # show the graph
            # pos = nx.spring_layout(G)  # You can use different layout algorithms
            # nx.draw_networkx(G, pos=pos, with_labels=False, node_size=10)
            # plt.show()

            # graph_data = gdata(x=features, edge_index=torch.tensor(list(G.edges)).t().contiguous())
            # graph_data = gdata(x=features, edge_index=on_voxels) # Create a PyTorch Geometric Data object
            # # assigning labels to each graph # for experimenting, generating random labels
            # graph_data.y = torch.randint(0, 2, (1,)).long()

            # self.Graph_data_list.append(graph_data)

    def print_graph_data_info(self):
        # Gather about the features and classes
        print(f'Dataset: {self.Graph_data_list}:')
        print('======================')
        print(f'Number of graphs: {len(self.Graph_data_list)}')
        # print(f'Number of features: {self.Graph_data_list.num_features}')
        # print(f'Number of classes: {self.Graph_data_list.num_classes}')

        for d in self.Graph_data_list:
            print("-------------------")
            print(f'Number of nodes: {d.num_nodes}')
            print(f'Number of edges: {d.num_edges}')
            print(f'Average node degree: {d.num_edges / d.num_nodes:.2f}')
            # print(f'Number of training nodes: {d.train_mask.sum()}')
            # print(f'Training node label rate: {int(d.train_mask.sum()) / d.num_nodes:.2f}')
            print(f'Has isolated nodes: {d.has_isolated_nodes()}')
            print(f'Has self-loops: {d.has_self_loops()}')
            print(f'Is undirected: {d.is_undirected()}')

    def visualize_graph(self, G, color):
        plt.figure(figsize=(7,7))
        plt.xticks([])
        plt.yticks([])
        nx.draw_networkx(G, pos=nx.spring_layout(G, seed=42), with_labels=False,
                         node_color=color, cmap="Set2")
        plt.show()

# Define the Graph Classifier model
# Define the Graph Classifier model
class GraphClassifier(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GraphClassifier, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, forward_data):
        x, edge_index = forward_data.x, forward_data.edge_index

        x = self.conv1(x, edge_index)
        x = torch.relu(x)
        x = self.conv2(x, edge_index)
        x = global_add_pool(x, forward_data.batch)  # Global pooling to get a graph-level representation
        return x

    def learn_nilear(self):
        # plotting the image
        nilearn.plotting.plot_img(self.atlas)
        nilearn.plotting.show()

        # plotting glass
        plotting.plot_glass_brain(self.atlas, threshold=3)
        nilearn.plotting.show()

        # smoothing an image
        smooth_anat_img = image.smooth_img(self.atlas, fwhm=3)
        nilearn.plotting.plot_img(smooth_anat_img)
        nilearn.plotting.show()

        # plotting glass smoothing
        plotting.plot_glass_brain(smooth_anat_img, threshold=3)
        nilearn.plotting.show()

        # plotting connectome
        nilearn.plotting.plot_connectome(self.atlas)
        nilearn.plotting.show()

if __name__ == "__main__":
    ABIDE2_BNI_i = ABIDE2_BNI()

    # ################# printing Atlas #################
    plotting.plot_roi(ABIDE2_BNI_i.AAL_Atlas_img_data, cmap='Paired', draw_cross=False, annotate=True, colorbar=True)
    plotting.show()

    # region_label = 2001
    # region_mask = (ABIDE2_BNI_i.AAL_Atlas_bin_data == region_label).astype(np.uint8)
    # region_voxels = ABIDE2_BNI_i.AAL_Atlas_bin_data * region_mask
    # plotting.plot_roi(region_voxels, cmap='Paired', draw_cross=False, annotate=True, colorbar=True)
    # plotting.show()

    # print("Atlas bin shape data: ", ABIDE2_BNI_i.AAL_Atlas_bin_data.shape)
    # unique_labels = np.unique(ABIDE2_BNI_i.AAL_Atlas_bin_data)
    # #print("Labels: ", ABIDE2_BNI_i.AAL_Atlas_bin_data)
    # print("Unique labels in the atlas length: ", len(unique_labels))
    # print("Unique labels in the atlas:", unique_labels)

    # Load and save graph_data to a file
    ABIDE2_BNI_i.load_dataset()
    with open('C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\ds\\abide2\\ABIDE_source_BNI\\graph_data.pkl',
              'wb') as file:
        pickle.dump(ABIDE2_BNI_i.Graph_data_list, file)

    # Load saved data
    # with open('C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\abide2\\ABIDE_source_BNI\\graph_data.pkl', 'rb') as file:
    #     ABIDE2_BNI_i.Graph_data_list = pickle.load(file)

    # # ################# printing graph data ############
    # ABIDE2_BNI_i.print_graph_data_info()

    # visualize
    # print("------------> Graph_data_list[0].__dict__ ", ABIDE2_BNI_i.Graph_data_list[0].__dict__)
    # print("------------> Graph_data_list[0].edge_index.t() ", ABIDE2_BNI_i.Graph_data_list[0].edge_index.t())
    # G = to_networkx(ABIDE2_BNI_i.Graph_data_list[0], to_undirected=True)
    # ABIDE2_BNI_i.visualize_graph(G, ["red", "blue", "green"])

    # # Example usage:
    # model = GraphClassifier(in_channels=ABIDE2_BNI_i.Graph_data_list[0].x.size(1),
    #                         hidden_channels=64,
    #                         out_channels=2)  # Assuming binary classification
    #
    # # Define your loss function (e.g., CrossEntropyLoss) and optimizer (e.g., Adam)
    # criterion = torch.nn.CrossEntropyLoss()
    # optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    #
    # # Define the train Loader
    # train_loader = gdataLoader(ABIDE2_BNI_i.Graph_data_list, batch_size=30, shuffle=True)
    #
    # # Train the model
    # num_epochs = 10  # Adjust as needed
    # for epoch in range(num_epochs):
    #     model.train()
    #     for data in train_loader:
    #         print("x size:", data.x.size())
    #         print("edge_index size:", data.edge_index.size())
    #         print("y size:", data.y.size())
    #         optimizer.zero_grad()
    #         output = model(data)
    #         print("model output size: ", output.size())
    #         loss = criterion(output, data.y)
    #         loss.backward()
    #         optimizer.step()

    # # Evaluate the model on the test set
    # model.eval()
    # with torch.no_grad():
    #     for data in train_loader:  # Use test_loader in a real scenario
    #         output = model(data)
    #         predicted_labels = torch.argmax(output, dim=1)
    #         print("Predicted Labels:", predicted_labels.numpy())