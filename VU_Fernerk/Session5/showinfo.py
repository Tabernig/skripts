#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\
#activate rs
#File:
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Session5\showinfo.py -file D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\outfile.tif
#Folder: 
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Session5\showinfo.py -folder D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13 -endsWith .tif

# MODULS
import argparse
import rasterio
import matplotlib.pyplot as plt 
import numpy as np
import os


parser = argparse.ArgumentParser(description="this script prints filename, extent, datatype and basic statistics (min, max, mean) of given files. Give Path to folder for more than one File. Optional: give Ending.")

parser.add_argument("-file", type= str, help= "File to be checked")
parser.add_argument('-folder', type=str, help='Folder containig Files')
parser.add_argument("-endsWith",type=str, help= "(Optional) When only files of a given format should be checked in a FOLDER")

#parsing
args = parser.parse_args()

#recall of variables
print (args.file)
print (args.folder)
print (args.endsWith)


if type(args.file) == str:
    with rasterio.open(args.file,"r") as obj:
        print("Filename: ",obj.name)
        array = obj.read(1)  #numpy array
        print("Extent: ",array.shape)
        print("Data type: ",array.dtype)
        print("Min/Mean/Max: ", np.min(array),np.mean(array),np.max(array))
        print("\n")

if type(args.folder) == str:
    os.chdir(args.folder)
    for f in os.listdir(args.folder):
        if f.endswith(args.endsWith):
            with rasterio.open(f,"r") as obj:
                print("Filename: ",obj.name)
                array = obj.read(1)  #numpy array
                print("Extent: ",array.shape)
                print("Data type: ",array.dtype)
                print("Min/Mean/Max: ", np.min(array),np.mean(array),np.max(array))
                print("\n")
    






# for f_ in fileList:
#     with rasterio.open(f_,"r") as obj:
#             print("Adding ",obj, " to composite...")
#             array = obj.read(1)  #numpy array
#             maxA = np.max(array)
#             for x in range(shape[0]):
#                 for y in range(shape[1]):
#                     array[x,y] = array[x,y]
#                     if array[x,y] > 10000 or array[x,y]<0:
#                         continue
#                     Array3D[x,y][count] = int((array[x,y])/10000*255)
#             maxList.append(maxA)
#             # print(array.shape ,"Shape")
#             # print(array.dtype ,"\t dtype")
#             crsA = (obj.crs)
#             trans = obj.transform
#             # print(obj.nodata ,"\t nodata")
#             # print(obj.driver ,"\t driver")
#             # print("\n")
#    count += 1


