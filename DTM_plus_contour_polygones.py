import pandas as pd
import geopandas as gpd
import numpy as np
import rasterio as rio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from pyproj import CRS

# Define the British National Grid CRS (EPSG:27700)
british_national_grid = CRS.from_epsg(27700)

# Define the path of the file
asc_file_path = 'D:/Ulster/EGM722_Programming_for_GIS_and_Remote_Sensing/EGM722_Assesment/EGM722_Project/project/EGM722_Project_Data/DTM_asc/TL4358.asc'

# Open the .asc file
with rio.open(asc_file_path) as dataset:

    # Set the coordinate reference system to British National Grid (EPSG:27700)
    #dataset.crs = rasterio.crs.CRS({'init': 'epsg:27700'})


# Setting a DatasetReader object for reading the dataset and its attributes
dataset = rio.open('D:/Ulster/EGM722_Programming_for_GIS_and_Remote_Sensing/EGM722_Assesment/EGM722_Project/project/EGM722_Project_Data/DTM_asc/TL4358.asc')
# function that reads the .asc fies that contain the DTM raster info and transform them into geodataframe.
dtm = dataset.read()

print(dtm.crs)



# Setting a new CRS as 'British National Grid'='EPSG:27700'
# dataset.crs = rio.crs.CRS({'init': 'epsg:27700'})
