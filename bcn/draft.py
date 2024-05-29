## overlaying with another image

# # Overlay the resampled atlas on the original image
  # plotting.plot_roi(aal_atlas_resampled_img, bg_img=file_path, title="Resampled Atlas on Original Image")
  #
  # # Overlay the masked binary image on the original image
  # # plotting.plot_roi(nib.Nifti1Image(masked_binary_image, nii_img_data.affine), bg_img=file_path,
  # #                   title="Masked Binary Image on Original Image")
  # plotting.show()

## #####################################################################

## Thresholding by region
import numpy as np
import nibabel as nib
from nilearn.image import resample_img
from sklearn.preprocessing import MinMaxScaler

# Load the atlas and the original image
atlas_file_path = 'path_to_atlas.nii.gz'
image_file_path = 'path_to_image.nii.gz'

# Load the images
atlas_img = nib.load(atlas_file_path)
nii_img = nib.load(image_file_path)

# Resample the atlas to match the original image
atlas_resampled_img = resample_img(atlas_img, target_affine=nii_img.affine, target_shape=nii_img.shape)
atlas_resampled_data = atlas_resampled_img.get_fdata()

# Normalize the original image
nii_data = nii_img.get_fdata()
scaler = MinMaxScaler()
nii_data_normalized = scaler.fit_transform(nii_data.reshape(-1, 1)).reshape(nii_data.shape)

# Define a function to apply region-specific thresholding
def region_specific_thresholding(nii_data_normalized, atlas_data, region_value, threshold):
    region_mask = (atlas_data == region_value)
    thresholded_region = np.multiply(nii_data_normalized, region_mask)
    thresholded_region[thresholded_region < threshold] = 0
    return thresholded_region

# Initialize an empty array for the combined masked image
masked_image_combined = np.zeros_like(nii_data_normalized)

# Iterate through each region and apply thresholding
unique_rois = np.unique(atlas_resampled_data)
unique_rois = unique_rois[unique_rois != 0]  # Exclude the background (0)

for roi_value in unique_rois:
    # Define a specific threshold for this region (this example uses a fixed threshold for simplicity)
    threshold = 0.1  # Adjust this threshold value as needed
    thresholded_region = region_specific_thresholding(nii_data_normalized, atlas_resampled_data, roi_value, threshold)
    
    # Combine the thresholded regions
    masked_image_combined += thresholded_region

# Create a Nifti image for the combined masked image
masked_img_nifti = nib.Nifti1Image(masked_image_combined, affine=nii_img.affine)

# Plot the combined masked image
import nilearn.plotting as plotting

plotting.plot_img(masked_img_nifti, title="Region-Specific Thresholded Masked Image")
plotting.show()

## Graph construction
import numpy as np
import nibabel as nib
from nilearn.image import resample_img
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import cdist
import networkx as nx
import matplotlib.pyplot as plt

class BrainGraphConstructor:
    def __init__(self, atlas_path):
        self.atlas_path = atlas_path
        self.atlas_data = nib.load(atlas_path).get_fdata()
        self.unique_rois = np.unique(self.atlas_data)
        self.unique_rois = self.unique_rois[self.unique_rois != 0]  # Exclude background if labeled as 0

    def load_image(self, file_path, normalize=True):
        nii_image = nib.load(file_path)
        nii_data = nii_image.get_fdata()

        if normalize:
            scaler = MinMaxScaler()
            nii_data_normalized = scaler.fit_transform(nii_data.reshape(-1, 1)).reshape(nii_data.shape)
            return nii_image, nii_data, nii_data_normalized
        else:
            return nii_image, nii_data, nii_data

    def resample_atlas(self, target_affine, target_shape):
        atlas_img = nib.load(self.atlas_path)
        resampled_atlas_img = resample_img(atlas_img, target_affine=target_affine, target_shape=target_shape)
        return resampled_atlas_img.get_fdata()

    def region_specific_thresholding(self, image_data, atlas_data, roi_value, threshold):
        region_mask = (atlas_data == roi_value)
        region_data = image_data * region_mask
        thresholded_region = np.where(region_data > threshold, region_data, 0)
        return thresholded_region

    def construct_graph(self, file_path, distance_threshold=20.0):
        nii_img_data, nii_bin_data_original, nii_bin_data_normalized = self.load_image(file_path, normalize=True)
        atlas_resampled_data = self.resample_atlas(nii_img_data.affine, nii_bin_data_original.shape)

        masked_image_combined = np.zeros_like(nii_bin_data_normalized)
        
        for roi_value in self.unique_rois:
            threshold = 0.1  # Define a specific threshold for this region if needed
            thresholded_region = self.region_specific_thresholding(nii_bin_data_normalized, atlas_resampled_data, roi_value, threshold)
            masked_image_combined += thresholded_region

        unique_rois = np.unique(atlas_resampled_data)
        unique_rois = unique_rois[unique_rois != 0]

        roi_centroids = []
        for roi_value in unique_rois:
            roi_voxels = np.column_stack(np.where(atlas_resampled_data == roi_value))
            if roi_voxels.size == 0:
                continue
            centroid = np.mean(roi_voxels, axis=0)
            roi_centroids.append(centroid)

        roi_centroids = np.array(roi_centroids)

        G = nx.Graph()
        for i, centroid in enumerate(roi_centroids):
            G.add_node(i, centroid=centroid, label=unique_rois[i])

        distances = cdist(roi_centroids, roi_centroids, 'euclidean')
        for i in range(len(roi_centroids)):
            for j in range(i+1, len(roi_centroids)):
                if distances[i, j] <= distance_threshold:
                    G.add_edge(i, j, weight=distances[i, j])

        return G

    def plot_graph(self, G, output_file='brain_graph.png'):
        pos = {i: (G.nodes[i]['centroid'][0], G.nodes[i]['centroid'][1]) for i in G.nodes}
        plt.figure(figsize=(10, 10))
        nx.draw(G, pos, with_labels=True, node_size=50, node_color='blue', font_size=8, edge_color='gray')
        plt.savefig(output_file)
        plt.show()

# Usage
atlas_path = 'path/to/aal_atlas.nii'
image_path = 'path/to/subject_image.nii'
brain_graph_constructor = BrainGraphConstructor(atlas_path)
G = brain_graph_constructor.construct_graph(image_path, distance_threshold=20.0)
brain_graph_constructor.plot_graph(G)

##########################################################################
import numpy as np
import nibabel as nib
from nilearn.image import resample_img
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import cdist
import networkx as nx
import matplotlib.pyplot as plt

class BrainGraphConstructor:
    def __init__(self, atlas_path):
        self.atlas_path = atlas_path
        self.atlas_data = nib.load(atlas_path).get_fdata()
        self.unique_rois = np.unique(self.atlas_data)
        self.unique_rois = self.unique_rois[self.unique_rois != 0]  # Exclude background if labeled as 0

    def load_image(self, file_path, normalize=True):
        nii_image = nib.load(file_path)
        nii_data = nii_image.get_fdata()

        if normalize:
            scaler = MinMaxScaler()
            nii_data_normalized = scaler.fit_transform(nii_data.reshape(-1, 1)).reshape(nii_data.shape)
            return nii_image, nii_data, nii_data_normalized
        else:
            return nii_image, nii_data, nii_data

    def resample_atlas(self, target_affine, target_shape):
        atlas_img = nib.load(self.atlas_path)
        resampled_atlas_img = resample_img(atlas_img, target_affine=target_affine, target_shape=target_shape)
        return resampled_atlas_img.get_fdata()

    def region_specific_thresholding(self, image_data, atlas_data, roi_value, threshold):
        region_mask = (atlas_data == roi_value)
        region_data = image_data * region_mask
        thresholded_region = np.where(region_data > threshold, region_data, 0)
        return thresholded_region

    def construct_graph(self, file_path, distance_threshold=20.0):
        nii_img_data, nii_bin_data_original, nii_bin_data_normalized = self.load_image(file_path, normalize=True)
        atlas_resampled_data = self.resample_atlas(nii_img_data.affine, nii_bin_data_original.shape)

        masked_image_combined = np.zeros_like(nii_bin_data_normalized)
        
        for roi_value in self.unique_rois:
            threshold = 0.1  # Define a specific threshold for this region if needed
            thresholded_region = self.region_specific_thresholding(nii_bin_data_normalized, atlas_resampled_data, roi_value, threshold)
            masked_image_combined += thresholded_region

        # Calculate centroids of the combined masked regions
        unique_masked_rois = np.unique(masked_image_combined)
        unique_masked_rois = unique_masked_rois[unique_masked_rois != 0]  # Exclude background

        roi_centroids = []
        for roi_value in unique_masked_rois:
            roi_voxels = np.column_stack(np.where(masked_image_combined == roi_value))
            if roi_voxels.size == 0:
                continue
            centroid = np.mean(roi_voxels, axis=0)
            roi_centroids.append(centroid)

        roi_centroids = np.array(roi_centroids)

        # Construct the graph
        G = nx.Graph()
        for i, centroid in enumerate(roi_centroids):
            G.add_node(i, centroid=centroid, label=unique_masked_rois[i])

        distances = cdist(roi_centroids, roi_centroids, 'euclidean')
        for i in range(len(roi_centroids)):
            for j in range(i+1, len(roi_centroids)):
                if distances[i, j] <= distance_threshold:
                    G.add_edge(i, j, weight=distances[i, j])

        return G

    def plot_graph(self, G, output_file='brain_graph.png'):
        pos = {i: (G.nodes[i]['centroid'][0], G.nodes[i]['centroid'][1]) for i in G.nodes}
        plt.figure(figsize=(10, 10))
        nx.draw(G, pos, with_labels=True, node_size=50, node_color='blue', font_size=8, edge_color='gray')
        plt.savefig(output_file)
        plt.show()

# Usage
atlas_path = 'path/to/aal_atlas.nii'
image_path = 'path/to/subject_image.nii'
brain_graph_constructor = BrainGraphConstructor(atlas_path)
G = brain_graph_constructor.construct_graph(image_path, distance_threshold=20.0)
brain_graph_constructor.plot_graph(G)
