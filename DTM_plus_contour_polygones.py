import pandas as pd
import geopandas as gpd

# read the .asc fies that contain the DTM raster info
df = gpd.read_file('EGM722_Project_Data/DTM_asc/TL4358.asc')
df.head(5)

