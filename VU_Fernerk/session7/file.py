import os
from pathlib import Path

import geopandas as gpd
import rasterio
from rasterio import features

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

def read_img(path_to_img):
    with rasterio.open(path_to_img, "r") as img:
        return img.read(1).astype(np.float32)
        

# vector data from last session
gt = gpd.read_file("D:\_Programmieren\VU_Automatisierung_Daten\Daten\session7\data\ground_truth_vector")

# satellite data from last session
base = Path("D:\_Programmieren\VU_Automatisierung_Daten\Daten\session7\data\s2_img")





