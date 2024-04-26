import pandas as pd
import geopandas as gpd
import numpy as np
import rasterio as rio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from pyproj import CRS

# Define the CRS, in this case British National Grid CRS (EPSG:27700)
british_national_grid = CRS.from_epsg(27700)

# Define the path of the file
asc_file_path = 'D:/Ulster/EGM722_Programming_for_GIS_and_Remote_Sensing/EGM722_Assesment/EGM722_Project/project/EGM722_Project_Data/DTM_asc/TL4358.asc'

# Setting a DatasetReader object for reading the dataset and its attributes
with rio.open(asc_file_path) as dataset:
    if dataset.crs is None:
        # Ask the user to specify the Coordinate Reference System (CRS)
        new_crs = input(f"CRS is not specified for '{dataset.name}'. Please specify a CRS (e.g., 'EPSG:27700'): ")
        print(f"The specified crs for the file is {new_crs}")

        # Update the dataset's profile with the new CRS
        profile = dataset.profile
        profile['crs'] = new_crs

        # Read the data
        data = dataset.read()

        # Write the data with the updated profile
        with rio.open('new_raster.asc', 'w', **profile) as dst:
            dst.write(data)
            print(dst.crs)
    else:
        print(f"CRS is specified for '{dataset.name}': {dataset.crs}")

# function that reads the .asc fies that contain the DTM raster info and transform them into geodataframe.
#dtm = dataset.read('crs':)
#print(dtm.crs)
