#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\
#activate rs
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Session5\composite.py -band1 D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\T32TPT_20200913T101629_B02_10m.tif -band2 D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\T32TPT_20200913T101629_B03_10m.tif -band3 D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\T32TPT_20200913T101629_B04_10m.tif -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\outfile.tif

# MODULS
import argparse
import rasterio
import matplotlib.pyplot as plt 
import numpy as np
