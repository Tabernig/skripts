#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6
#activate rs



#import

import numpy as np
import matplotlib.pyplot as plt
import os
import rasterio
from pathlib import Path                                    #Alternative zum OS für Pfade
from pprint import pprint as pp
from sklearn.ensemble import RandomForestClassifier as RF   #Random Forest Klassifikator
from sklearn.model_selection import train_test_split        #Für Einteilung des Datensatzes in Trainings- und Validierungsdatensatzes
from sklearn.metrics import plot_confusion_matrix           #
import time
import pandas as pd
from sklearn.inspection import permutation_importance

bands10m = ["B02","B03","B04","B05","B06","B07","B08","B11","B08","B12","NDVI","NDSI"]
path_sat_img = Path("D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\s2_img_exercise")

#training und test daten

training_vector = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\\train_test_vector\ground_truth.gpkg"
training_raster = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\\train_test_raster\ground_truth.tif"


# rasterize training and test data
xmin, ymin, xmax, ymax = 654000, 5200140, 672760, 5227400
res = 10
datatype_out = "Int16"
burn_field = "class_id"
nodata = "-1"


cmd = f"gdal_rasterize -a {burn_field} -of GTiff -te {xmin} {ymin} {xmax} {ymax} -tr {res} {res} -a_nodata {nodata} -ot {datatype_out} {training_vector} {training_raster}"
print(cmd)

os.system(cmd)

print("Done.")

#write function to return bands
def read_img(path_to_img):
        with rasterio.open(path_to_img, "r") as img:
            return img.read(1).astype(np.float32)


#read bands
bands = []
for f in path_sat_img.glob("*tif"):
    band_id = f.stem.split("_")[2]
    if band_id in bands10m:
        print(f)
        bands.append(read_img(f))

bands = np.dstack(bands)

#read metadata
template = {}

with rasterio.open(training_raster,"r") as img:
    template["transform"] = img.transform
    template["crs"] = img.crs


#labels laden

labels = read_img(training_raster)
print(labels.shape)
print(np.unique(labels, return_counts = True)) #zeigt uns die Einzelnen Werte des Bildes
#Als Referenz: 
mapping = {
0: "rock_debris",
1: "forest",
2: "grassland",
3: "ice_snow"
}

#reshape
labels_1d = labels[labels>=0].reshape((-1))
print(labels_1d.shape)


#split into 
X = bands[labels>=0,:]
y= labels_1d
feature_names = [f'feature {i}' for i in range(X.shape[1])]
X_train, X_test,y_train,y_test = train_test_split(bands[labels>=0,:],labels_1d,test_size=0.3,random_state=0, shuffle=True)


rf = RF(n_estimators=50, n_jobs=-1,oob_score=True)



rf.fit(X_train, y_train)

start_time = time.time()
importances = rf.feature_importances_
std = np.std([
    tree.feature_importances_ for tree in rf.estimators_], axis=0)
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: "
      f"{elapsed_time:.3f} seconds")

forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()
plt.show()


start_time = time.time()
result = permutation_importance(
    rf, X_test, y_test, n_repeats=10, random_state=0, n_jobs=-1)
elapsed_time = time.time() - start_time
print(f"Elapsed time to compute the importances: "
      f"{elapsed_time:.3f} seconds")

forest_importances = pd.Series(result.importances_mean, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Feature importances using permutation on full model")
ax.set_ylabel("Mean accuracy decrease")
fig.tight_layout()
plt.show()



rows, cols, n_bands = bands.shape

X_pred = bands.reshape((rows*cols,n_bands))

y_pred = rf.predict(X_pred)

y_pred_2d = y_pred.reshape((rows,cols))

with rasterio.open("prediciton-UE1.tif",
    "w",
    driver="GTiff",
    height=y_pred_2d.shape[0],
    width=y_pred_2d.shape[1],
    count = 1,
    dtype = y_pred_2d.dtype,
    crs = template["crs"],
    transform = template["transform"]) as fobj:
    fobj.write(y_pred_2d, 1)



print("Done")