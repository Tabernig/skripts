import os
from pathlib import Path
import numpy as np
np.set_printoptions(suppress=True)
import pandas as pd
import matplotlib.pyplot as plt

from scipy.signal import savgol_filter
from scipy.optimize import curve_fit
from scipy import integrate
base = Path("D:\_Programmieren\VU_Automatisierung_Daten\Daten\session8\data")


for f in base.glob("*npy"):
    print(f.absolute())


ndvi = np.load("D:\_Programmieren\VU_Automatisierung_Daten\Daten\session8\data\\ndvi.npy")
scl = np.load("D:\_Programmieren\VU_Automatisierung_Daten\Daten\session8\data\scl.npy")
time = np.load("D:\_Programmieren\VU_Automatisierung_Daten\Daten\session8\data\\time.npy")