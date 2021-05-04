# MODULS
import rasterio
import matplotlib.pyplot as plt 
import numpy as np
import os

#created predictions
path = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\s2_img_exercise\estimates\"prediciton-UE2"
nList = [10,20,50]+list(range(100,2001,100))
# +str(n)+".tif

#trainingdataset
pathTrain = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\\train_test_raster\ground_truth.tif"

accuracyDict = {}
#get Shape
with rasterio.open(pathTrain,"r") as reference:
    refAr = reference.read(1)
    for n in nList:
        accCount = 0
        with rasterio.open(path+str(n)+".tif","r") as check:
            checkAr = check.read(1)
            for x in refAr:
                for y in x:
                    if refAr[x,y] == checkAr[x,y]:
                        accCount += 1
        accuracyDict[n] = accCount

######### Plot ########
plt.plot(x,y)
plt.title("Out of bag Accuracy")
plt.show()
