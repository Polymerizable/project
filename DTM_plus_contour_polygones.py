import pandas as pd
import geopandas as gpd
import numpy as np
import rasterio as rio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from pyproj import CRS

# Define the British National Grid CRS (EPSG:27700)
british_national_grid = CRS.from_epsg(27700)

# Setting a new CRS as 'British National Grid'='EPSG:27700'
dataset.crs = rio.crs.CRS({'init': 'epsg:27700'})
# function that reads the .asc fies that contain the DTM raster info and transform them into geodataframe.
dtm = rio.read_file('EGM722_Project_Data/DTM_asc/TL4358.asc')

# Set the CRS to the dataset (two ways for doing it)
dtm = gdf.set_crs(british_national_grid) is a second way to set
dtm = gdf.set_crs("EPSG:27700")  # this sets the coordinate reference system to epsg:27700, wgs84 lat/lon
