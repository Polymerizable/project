import pandas as pd
import geopandas as gpd
import numpy as np
import rasterio as rio
import rasterio.features
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from pyproj import CRS
import os
from shapely.geometry import shape

# Define the CRS, in this case British National Grid CRS (EPSG:27700)
selected_crs = CRS.from_epsg(27700)

# Define folder path. The second option is to ask for it
folder_path = 'D:/Ulster/EGM722_Programming_for_GIS_and_Remote_Sensing/EGM722_Assesment/EGM722_Project/project/EGM722_Project_Data/DTM_asc/new_crs_subfolder'
#  folder_path = imput("Please introduce the folder path that contain the data:")

while True:
    #  Ask for the water flood expected level.
    flood_level = input("Please enter the expected water flood level (meters):")
    # Check if the input is a valid floating-point number
    try:
        flood_level_input = float(flood_level)
        break
    except ValueError:
        print("Invalid input. Please enter a valid floating-point number.")

# Create a list with all the files in the folder
files = os.listdir(folder_path)

# Iterate through each file in the folder to work with them
for file_name in files:
    # Split the file_name into base_name and extension
    base_name, extension = os.path.splitext(file_name)

    if extension == '.tif':
        # Define the path of the file
        file_path = os.path.normpath(os.path.join(folder_path, file_name))

        with rio.open(file_path) as dataset:
            # Read the raster data as a numpy array
            data = dataset.read()

            # Create a mask to select pixels with values higher than the threshold
            mask = data <= flood_level_input

            mask = np.where(mask, 1, 0)  # Convert True to 1, False to 0

            # Generate shapes from the mask
            shapes_generated = rasterio.features.shapes(mask, transform=dataset.transform)

            # Convert shapes to polygons
            polygons = [shape(geom) for geom, value in shapes_generated if value == 1]

            # Create a GeoDataFrame from the polygons
            gdf = gpd.GeoDataFrame(geometry=polygons, crs=dataset.crs)

            # Save the GeoDataFrame to a shapefile
            output_shapefile = os.path.normpath(os.path.join(folder_path, base_name + '.shp'))
            gdf.to_file(output_shapefile)