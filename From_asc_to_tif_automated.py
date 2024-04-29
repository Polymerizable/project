import rasterio as rio
from pyproj import CRS
import os

# Define the CRS, in this case British National Grid CRS (EPSG:27700)
new_crs = CRS.from_epsg(27700)

# Define folder path
folder_path = 'D:/Ulster/EGM722_Programming_for_GIS_and_Remote_Sensing/EGM722_Assesment/EGM722_Project/project/EGM722_Project_Data/DTM_tif'

# Create a list with all the files in the folder
files = os.listdir(folder_path)

# Iterate through each file in the folder to work with them
for file_name in files:
    # Define the path of the file
    asc_file_path = os.path.normpath(os.path.join(folder_path, file_name))

    # Split the file_name into base_name and extension
    base_name, extension = os.path.splitext(file_name)

    # checking if the file is .asc
    if extension.lower() == '.asc':
        # Setting a DatasetReader object for reading the dataset and its attributes
        with rio.open(asc_file_path) as dataset:
            # Define the new file name that will go in the 'subfolder_path'
            output_folder = folder_path
            output_file = os.path.normpath(os.path.join(output_folder, "new_crs_" + base_name + ".tif"))

            # Create the file if it doesn't exist in the new subfolder
            if not os.path.exists(output_file):
                if dataset.crs is None:
                    # Update the dataset's profile with the new CRS
                    profile = dataset.profile
                    profile['crs'] = new_crs
                    profile['driver'] = 'GTiff'

                    # Read the data
                    data = dataset.read()

                    # Write the data with the updated profile
                    with rio.open(output_file, 'w', **profile) as dst:
                        dst.write(data)

                else:
                    print(f"CRS is specified for '{dataset.name}': {dataset.crs}")
                    print(f"Generating new file into the subfolder '{subfolder_path_normalised}")

                    # Write the data with the updated name to have all the files in the new subfolder
                    with rio.open(output_file, 'w', 'GTiff') as dst:
                        data = dataset.read()
                        dst.write(data)