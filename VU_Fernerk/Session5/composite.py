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
parser.add_argument('-outfile', type=str, help='(optional) output file')
parser.add_argument("-histogram", type=str, help= "(optional) Histogram, y if needed")

#parsing
args = parser.parse_args()

#recall of variables

print (args.band1)
print (args.band2)
print (args.band3)
print (args.outfile)
print (args.histogram)

fileList = [args.band1,args.band2,args.band3]

#get Shape
with rasterio.open(args.band1,"r") as check:
            #print(check)
            temparray = check.read(1)
            shape = temparray.shape

Array3D = np.zeros(shape+(3,),dtype=np.uint8)  # make array 3d

count = 0
maxList = []
for f_ in fileList:
    with rasterio.open(f_,"r") as obj:
            print("Adding ",obj, " to composite...")
            array = obj.read(1)  #numpy array
            maxA = np.max(array)
            for x in range(shape[0]):
                for y in range(shape[1]):
                    array[x,y] = array[x,y]
                    if array[x,y] > 10000 or array[x,y]<0:
                        continue
                    Array3D[x,y][count] = int((array[x,y])/10000*255)
            maxList.append(maxA)
            # print(array.shape ,"Shape")
            # print(array.dtype ,"\t dtype")
            crsA = (obj.crs)
            trans = obj.transform
            # print(obj.nodata ,"\t nodata")
            # print(obj.driver ,"\t driver")
            # print("\n")
    count += 1

plt.figure()
plt.title("Composite")
ax = plt.imshow(Array3D,vmin = 0, vmax = 255)        #beschreibt subplot aber nicht axis
#plt.colorbar()
plt.show()

######## change array shape in order for rasterio to write it properly ###############
Array3D = np.moveaxis(Array3D.squeeze(),-1,0)

###### Histogramm #######
if args.histogram == "y" or args.histogram == "Y":
    plt.figure()
    plt.title("Composite-Histogram")
    plt.hist(Array3D.ravel(),bins=100)
    plt.show()

#### Write Raster to chosen path
if args.outfile:
    with rasterio.open(args.outfile,
        "w",
        driver="GTiff",
        height= shape[0],
        width= shape[1],
        count= 3,
        dtype= Array3D.dtype,
        crs= crsA,
        transform= trans
        ) as obj:
        obj.write(Array3D)
else:
    print("No Path for the outfile given...")


print("Done.")