# uebung6_eigenfeatures.py using scipy.spatial and own fuctions for covariance matrix
#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt
#activate rs
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Session5\composite.py -band1 D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\T32TPT_20200913T101629_B02_10m.tif -band2 D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\T32TPT_20200913T101629_B03_10m.tif -band3 D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\T32TPT_20200913T101629_B04_10m.tif -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\outfile.tif

# MODULS
import argparse
import rasterio
import matplotlib.pyplot as plt 
import numpy as np


parser = argparse.ArgumentParser(description='this script composites 3 Bands and creates a plot and optionaly allows to save the image to a defined path.')
parser.add_argument('-band1', type=str, help='Band 1')
parser.add_argument('-band2', type=str, help='Band 2')
parser.add_argument('-band3', type=str,  help='Band 3')
parser.add_argument('-outfile', type=str, help='output file')

#parsing
args = parser.parse_args()

#recall of variables
print (args.band1)
print (args.band2)
print (args.band3)
print (args.outfile)

fileList = [args.band1,args.band2,args.band3]

with rasterio.open(args.band1,"r") as check:
            print(check)
            temparray = check.read(1)
            shape = temparray.shape
print(shape, "###########################################")
baseArray = np.zeros(shape)
print(baseArray)

for f_ in fileList:
    with rasterio.open(f_,"r") as obj:
            print(obj)
            array = obj.read(1)  #numpy array
            baseArray += array
            print(array.shape ,"Shape")
            print(array.dtype ,"\t dtype")
            print(obj.crs ,"\t crs")
            print(obj.transform ,"\t transform")
            print(obj.nodata ,"\t nodata")
            print(obj.driver ,"\t driver")
            print("\n")



for x in baseArray:
    for y in x:
        if (y > 10000) or (y < 0):
            y = -99999
minB = baseArray.min()
maxB = baseArray.max() 
print(minB,maxB)

compArray = np.copy(baseArray)

compArray/compArray.max()*255

plt.figure()
plt.title(args.outfile)
ax = plt.imshow(compArray,vmin = 0, vmax = 255)        #beschreibt subplot aber nicht axis
plt.colorbar()
#plt.savefig("D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\my_img.jpg,",dpi = 200)
plt.show()



print(compArray)

#print(fileList)

print("Done.")