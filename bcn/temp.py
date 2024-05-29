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
