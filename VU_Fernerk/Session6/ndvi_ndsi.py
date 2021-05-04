
# MODULS
import rasterio
import matplotlib.pyplot as plt 
import numpy as np
import os

NIR = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\s2_img_exercise\T32TPT_20200913T101629_B08_10m.tif"
Red = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\s2_img_exercise\T32TPT_20200913T101629_B04_10m.tif"

SWIR = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\s2_img_exercise\T32TPT_20200913T101629_B11_20m.tif"
Green = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\s2_img_exercise\T32TPT_20200913T101629_B03_10m.tif"

outfile =  "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\s2_img_exercise\T32TPT_20200913T101629_ndvi.tif"
outfile2 =  "D:\_Programmieren\VU_Automatisierung_Daten\Daten\session6\s2_img_exercise\T32TPT_20200913T101629_ndsi.tif"

fileList = [Red, NIR, Green, SWIR]



#get Shape
with rasterio.open(Red,"r") as check:
            #print(check)
            temparray = check.read(1)
            shape = temparray.shape
            print(shape)
            crsA = check.crs
            trans = check.transform

NDVI = np.zeros(shape,dtype=rasterio.float32)  # make array 
NDSI = np.zeros(shape,dtype=rasterio.float32)  # make array 

count = 0
maxList = []
for f_ in fileList:
    with rasterio.open(f_,"r") as obj:
        #print("############################")
        #checkShape = obj.read(1)
        #shapeC = checkShape.shape
        #print(shapeC)
        #print("Adding ",obj, " to calculate NDVI(NDSI")
        if count == 0:
            redAr = obj.read(1)  #numpy array
        elif count == 1:
            print("NIR")
            nirAr = obj.read(1)  #numpy array
        elif count == 2:
            greenAr = obj.read(1)  #numpy array
        else:
            swirAr = obj.read(1)
    count += 1
#print(redAr,nirAr,greenAr,swirAr)



NDVI = (nirAr.astype(float)-redAr.astype(float))/(nirAr+redAr)
NDSI = (greenAr.astype(float)-swirAr.astype(float))/(greenAr+swirAr)

######## change array shape in order for rasterio to write it properly ###############
# NDVI = np.moveaxis(NDVI.squeeze(),-1,0)
# NDSI = np.moveaxis(NDSI.squeeze(),-1,0)


toPlotAndHist = [NDVI,NDSI]
for fobj in toPlotAndHist:
    ######### Plot ########
    plt.figure()
    plt.title("Index")
    ax = plt.imshow(fobj)        #beschreibt subplot aber nicht axis
    plt.colorbar()
    plt.show()

    ###### Histogramm #######
    plt.figure()
    plt.title("Histogram")
    plt.hist(fobj.ravel(),bins=50)
    plt.show()





#### Write Raster to chosen path

with rasterio.open(outfile,
    "w",
    driver="GTiff",
    height= shape[0],
    width= shape[1],
    count= 1,
    dtype= NDVI.dtype,
    crs= crsA,
    transform= trans
    ) as obj:
    obj.write(NDVI,1)

with rasterio.open(outfile2,
    "w",
    driver="GTiff",
    height= shape[0],
    width= shape[1],
    count= 1,
    dtype= NDSI.dtype,
    crs= crsA,
    transform= trans
    ) as obj:
    obj.write(NDSI,1)

#print(NDVI)
#print(NDSI)
print("Done.")