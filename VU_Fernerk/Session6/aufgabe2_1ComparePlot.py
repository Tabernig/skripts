# MODULS
import rasterio
import matplotlib.pyplot as plt 
import numpy as np
import os

#created predictions
path = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\s2_img_exercise\estimates\prediciton-UE2"
nList = [10,20,50]+list(range(100,1601,100))
# +str(n)+".tif

#trainingdataset
pathTrain = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\\train_test_raster\ground_truth.tif"

accuracyDict = {}
#get Shape
with rasterio.open(pathTrain,"r") as reference:
    refAr = reference.read(1)
    shape = reference.shape
    # height = reference.height, does not work somehow
    # width = reference.width,
    height = 2726
    width = 1876
    print(height,"\n",width)
    
    for n in nList:
        accCount = 0
        with rasterio.open(path+str(n)+".tif","r") as check:
            checkAr = check.read(1)
            for x in range(width):
                for y in range(height):
                    #print(refAr,checkAr)
                    if refAr[y,x] == checkAr[y,x]:
                        accCount += 1
        print(n,"done")
        accuracyDict[n] = accCount
print(accuracyDict)

######### Plot ########
lists = sorted(accuracyDict.items())
a, b = zip(*lists)

plt.plot(a,b)
plt.title("Out of bag Accuracy")
plt.show()
