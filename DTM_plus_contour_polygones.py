import pandas as pd
import geopandas as gpd
import numpy as np
import rasterio as rio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


# function that reads the .asc fies that contain the DTM raster info and transform them into geodataframe.
gdf = rio.read_file('EGM722_Project_Data/DTM_asc/TL4358.asc')
gdf.head(5)

gdf = gdf.set_crs("EPSG:27700")  # this sets the coordinate reference system to epsg:27700, wgs84 lat/lon
