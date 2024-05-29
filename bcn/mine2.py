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

    def load_image(self, file_path, normalize=False):
        # Loading the image
        nii_image_data = nib.load(file_path)

        # Get original image in binary format
        nii_bin_data_original = nii_image_data.get_fdata() # image is converted into NumPy arrays

        # Normalize values between [-1, 1]
        if normalize:
            scaler = MinMaxScaler()
            nii_bin_data_normalized = scaler.fit_transform(nii_bin_data_original.reshape(-1, 1)).reshape(nii_bin_data_original.shape)

        return nii_image_data, nii_bin_data_original, nii_bin_data_normalized

    def save_image(self, image_data, slice, filename):
        plt.imsave(filename, image_data[..., slice])

    # Define a function to apply region-specific thresholding
    def region_specific_thresholding(self, nii_data_normalized, atlas_data, region_value, threshold):
        region_mask = (atlas_data == region_value)
        thresholded_region = np.multiply(nii_data_normalized, region_mask)
        thresholded_region[thresholded_region < threshold] = 0
        return thresholded_region

    # Function to plot image slices
    def plot_img_slices(self, img_data, title="Image Slice"):
        fig, axes = plt.subplots(1, 3)
        axes[0].imshow(img_data[img_data.shape[0] // 2, :, :], cmap='gray')
        axes[0].set_title(f'{title} - Sagittal')
        axes[1].imshow(img_data[:, img_data.shape[1] // 2, :], cmap='gray')
        axes[1].set_title(f'{title} - Coronal')
        axes[2].imshow(img_data[:, :, img_data.shape[2] // 2], cmap='gray')
        axes[2].set_title(f'{title} - Axial')
        plt.show()

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

    def plot_graph(self, G, output_file='brain_graph.png'):
        pos = {i: (G.nodes[i]['centroid'][0], G.nodes[i]['centroid'][1]) for i in G.nodes}
        plt.figure(figsize=(10, 10))
        nx.draw(G, pos, with_labels=True, node_size=50, node_color='blue', font_size=8, edge_color='gray')
        plt.savefig(output_file)
        plt.show()

    def load_dataset(self):
        """ #############################################
                Getting some information about the Atlass before processing
            #############################################
        """ 
        atlas_original_unique_labels = np.unique(ABIDE2_BNI_i.AAL_Atlas_bin_data)
        print("-----------------------> Atlas Information")
        print("Atlas bin shape data: ", ABIDE2_BNI_i.AAL_Atlas_bin_data.shape)
        print("Unique labels in the atlas length: ", len(atlas_original_unique_labels))
        print("Unique labels in the atlas: ", atlas_original_unique_labels)

        # load exam data
        for i, file_path in enumerate(self.img_path_list_anat[:1]):
            """ #############################################
                Getting the image 
                #############################################
            """            
            # get the image data and the bin data
            nii_img_data, nii_bin_data_original, nii_bin_data_normalized = self.load_image(file_path, normalize=True)
            plotting.plot_img(nii_img_data, title="Original image")

            """ #############################################
                Processing Atlas image 
                #############################################
            """
            # Resample AAL atlas to match the resolution of the images and convert to binary array 
            # (using nearest neighbor interpolation to preserve labels)
            aal_atlas_resampled_img = resample_img(nib.load(self.atlas), target_affine=nii_img_data.affine, target_shape=nii_bin_data_normalized.shape, interpolation='nearest')
            aal_atlas_resampled_data = aal_atlas_resampled_img.get_fdata()
            aal_atlas_resampled_data = aal_atlas_resampled_data.astype(int)
            scaler = MinMaxScaler()
            aal_atlas_data_resampled_normalized = scaler.fit_transform(aal_atlas_resampled_data.reshape(-1, 1)).reshape(
                aal_atlas_resampled_data.shape)

            # logging and printing
            atlas_resampled_normalized_unique_rois = np.unique(aal_atlas_data_resampled_normalized)
            atlas_resampled_normalized_unique_rois = atlas_resampled_normalized_unique_rois[atlas_resampled_normalized_unique_rois != 0]
            print("-----------------> 1 atlas resampled information:")
            print("aal_atlas_data_resampled_normalized: ", aal_atlas_data_resampled_normalized.shape)
            print("Unique labels in the atlas resampled and normalized length: ", len(atlas_resampled_normalized_unique_rois))
            print("Unique labels in the atlas resampled and normalized: ", atlas_resampled_normalized_unique_rois)

            # Checking if there is any missing label in the resampled atlas
            missing_labels = set(atlas_original_unique_labels) - set(atlas_resampled_normalized_unique_rois)
            print(f"missing labels: {missing_labels}")

            # Optionally visualize the atlas
            # plotting.plot_img(ABIDE2_BNI_i.AAL_Atlas_img_data, title="Original Atlas")
            # plotting.plot_img(aal_atlas_resampled_img, title="Resampled Normalized Atlas")

            """ ################################################################
                Masking the image with Processing Atlas image with one threshold
                ################################################################
            """
            # # Masking image data with the Atlas using the numpy
            # masked_binary_image = np.multiply(nii_bin_data_normalized, aal_atlas_data_resampled_normalized > 0)
            #
            # # # Extract Unique ROIs from the Masked Image:
            # # masked_img_unique_rois = np.unique(masked_binary_image)
            # # masked_img_unique_rois = masked_img_unique_rois[masked_img_unique_rois != 0]
            # # print("--------------------> 2 one threshold masked image information")
            # # print("unique_rois in the masked image: ", len(masked_img_unique_rois))

            """ ################################################################
                Masking the image with processing Atlas with multiple threshold
                ################################################################
            """ 
            # Initialize an empty array for the combined masked image
            masked_image_combined = np.zeros_like(nii_bin_data_normalized)

            # Iterate through each region and apply thresholding
            for roi_value in atlas_resampled_normalized_unique_rois:
                # Define a specific threshold for this region (this example uses a fixed threshold for simplicity)
                threshold = 0.1 # 0 # to show everything #  # Adjust this threshold value as needed
                thresholded_region = self.region_specific_thresholding(nii_bin_data_normalized, aal_atlas_data_resampled_normalized, roi_value, threshold)
                
                # Combine the thresholded regions
                masked_image_combined += thresholded_region

            # Create a Nifti image for the combined masked image and plot it
            masked_img_nifti = nib.Nifti1Image(masked_image_combined, affine=nii_img_data.affine)
            # plotting.plot_img(masked_img_nifti, title="Region-Specific Thresholded Masked Image")

            # Showing separate regions
            # for r in [50, 55, 60]:
            #     masked_img_nifti_r = np.zeros_like(nii_bin_data_normalized)
            #     masked_img_nifti_r += masked_image_combined[r]
            #     masked_img_nifti_r_img = nib.Nifti1Image(masked_img_nifti_r, affine=nii_img_data.affine)
            #     plotting.plot_img(masked_img_nifti_r_img, title="Region-Specific Thresholded Masked Image" + str(r))
            #
            # plotting.show()

            """ ################################################################
                Constructing the graph from image
                ################################################################
            """
            # Calculate centroids of the combined masked regions
            unique_masked_rois = np.unique(masked_image_combined)
            unique_masked_rois = unique_masked_rois[unique_masked_rois != 0]  # Exclude background

            # get the unique ROIs from masked rois
            print("--------------> masked image unique rois information")
            print("unique_masked_rois: ", len(unique_masked_rois))

            roi_centroids = []
            for roi_value in unique_masked_rois:
                roi_voxels = np.column_stack(np.where(masked_image_combined == roi_value))
                if roi_voxels.size == 0:
                    continue
                centroid = np.mean(roi_voxels, axis=0)
                roi_centroids.append(centroid)

            print("number of centroids: ", len(roi_centroids))
            roi_centroids = np.array(roi_centroids)

            # Construct the graph
            G = nx.Graph()
            for i, centroid in enumerate(roi_centroids):
                G.add_node(i, centroid=centroid, label=unique_masked_rois[i])

            distances = cdist(roi_centroids, roi_centroids, 'euclidean')
            for i in range(len(roi_centroids)):
                for j in range(i + 1, len(roi_centroids)):
                    if distances[i, j] <= 10.0: #distance_threshold:
                        G.add_edge(i, j, weight=distances[i, j])

            self.plot_graph(G)
            """ ################################################################
                Some plotting
                ################################################################
            """
        
            # Show the masked image
            # plt.figure()
            # plt.imshow(masked_binary_image[:, :, masked_binary_image.shape[2] // 2], cmap='gray')
            # plt.title("Masked Binary Image")
            # plt.show()

            # # Visualize original image
            # self.plot_img_slices(nii_bin_data_original, title="Original Image")
            #
            # # Visualize resampled atlas
            # self.plot_img_slices(aal_atlas_resampled_data, title="Resampled Atlas")
            #
            # # Visualize the masked binary image
            # self.plot_img_slices(masked_binary_image, title="Masked Binary Image")


if __name__ == "__main__":
    ABIDE2_BNI_i = ABIDE2_BNI()

    # Loading dataset
    # Load and save graph_data to a file
    ABIDE2_BNI_i.load_dataset()
    # with open(
    #         'C:\\Users\\raids\\OneDrive\\Desktop\\my_phd\\Implementation\\ds\\abide2\\ABIDE_source_BNI\\graph_data.pkl',
    #         'wb') as file:
    #     pickle.dump(ABIDE2_BNI_i.Graph_data_list, file)

    # ################# printing Atlas #################
    # plotting.plot_roi(ABIDE2_BNI_i.AAL_Atlas_img_data, cmap='Paired', draw_cross=False, annotate=True, colorbar=True)
    # plotting.show()
    #
    # print("Atlas bin shape data: ", ABIDE2_BNI_i.AAL_Atlas_bin_data.shape)
    # unique_labels = np.unique(ABIDE2_BNI_i.AAL_Atlas_bin_data)
    # print("Unique labels in the atlas length: ", len(unique_labels))
    # print("Unique labels in the atlas:", unique_labels)

