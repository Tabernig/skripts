#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6
#activate rs
#File:
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Session5\showinfo_masked.py -file D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\outfile.tif


import numpy as numpy
import matplotlib.pyplot as plt
import os
import rasterio
from pathlib import Path
from pprint import pprint as pp
from sklearn.ensemble import RandomForestClassifier as RF 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import plot_confusion_matrix




print("Done.")