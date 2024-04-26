import pandas as pd
import geopandas as gpd
import numpy as np
import rasterio as rio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from pyproj import CRS
import os

# Define the CRS, in this case British National Grid (EPSG:27700)
british_national_grid = CRS.from_epsg(27700)

# Define folder path
folder_path = 'D:/Ulster/EGM722_Programming_for_GIS_and_Remote_Sensing/EGM722_Assesment/EGM722_Project/project/EGM722_Project_Data/DTM_asc'

# Create a list with all the files in the folder
files = os.listdir(folder_path)

# Iterate through each file in the folder to work with them
for file_name in files:

# Define the path of the file
asc_file_path = 'D:/Ulster/EGM722_Programming_for_GIS_and_Remote_Sensing/EGM722_Assesment/EGM722_Project/project/EGM722_Project_Data/DTM_asc/TL4358.asc'

# Setting a DatasetReader object for reading the dataset and its attributes
dataset = rio.open(asc_file_path)

if dataset.crs is None:
    new_crs = imput(f"CRS is not specified for '{file_name}'. Please specify a CRS (e.g., 'EPSG:27700'): ")


with rio.open(asc_file_path, mode="r+", crs="british_national_grid") as new_dataset:
    print(new_dataset.profile)

print(dataset.profile)
print(new_dataset.profile)
print(dataset.crs)

# function that reads the .asc fies that contain the DTM raster info and transform them into geodataframe.
#dtm = dataset.read()


dataset.close()
new_dataset.close()