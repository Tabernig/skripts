

#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13
import numpy
import os
from osgeo import gdal
import rasterio
import matplotlib.pyplot as plt 

#2      blue
#3      green
#4      red
#8      Near infrared
#scl    scene Classification 

##### Paths ########
dataFolder = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13"
filePath = "D:\_Programmieren\repos\skripts\VU_Fernerk\Abgaben\Session5\mitschrift.py"

os.chdir(dataFolder)

for f in os.listdir("D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13"):
    if f.endswith(".tif"):
        print(f)
        with rasterio.open(f,"r") as obj:
            print(obj)
            array = obj.read(1)  #numpy array
            print(array.shape ,"Shape")
            print(array.dtype ,"\t dtype")
            print(obj.crs ,"\t crs")
            print(obj.transform ,"\t transform")
            print(obj.nodata ,"\t nodata")
            print(obj.driver ,"\t driver")
            print("\n")

            # plt.figure()
            # plt.title(f)
            # ax = plt.imshow(array,vmin = 0, vmax = 3000)        #beschreibt subplot aber nicht axis
            # plt.colorbar()
            #plt.savefig("D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\my_img.jpg,",dpi = 200)
            #plt.show()

            ####### Histogramm #######
            plt.figure()
            plt.hist(array.ravel(),bins=100)
            plt.show()




