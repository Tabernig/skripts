#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\
#activate rs
#File:
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Session5\showinfo_masked.py -file D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\outfile.tif
#Folder: 
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Session5\showinfo_masked.py -folder D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13 -endsWith .tif
#Mask only:
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Session5\showinfo_masked.py -mask D:\_Programmieren\VU_Automatisierung_Daten\Daten\s2_ibk_2020-09-13\T32TPT_20200913T101629_SCL_10m.tif


# MODULS
import argparse
import rasterio
import matplotlib.pyplot as plt 
import numpy as np
import numpy.ma as ma
import os


parser = argparse.ArgumentParser(description="this script prints filename, extent, datatype and basic statistics (min, max, mean) of given files. Give Path to folder for more than one File. Optional: give Ending.")

parser.add_argument("-file", type= str, help= "File to be checked")
parser.add_argument('-folder', type=str, help='Folder containig Files')
parser.add_argument("-endsWith",type=str, help= "(Optional) When only files of a given format should be checked in a FOLDER")
parser.add_argument("-mask", type=str, help="Insert Mask")

#parsing
args = parser.parse_args()

#recall of variables
# print (args.file)
# print (args.folder)
# print (args.endsWith)
# print (args.mask)

def printInfos(file,returnYorN):
    print("Filename: ",obj.name)
    array = obj.read(1)  #numpy array
    print("Extent: ",array.shape)
    print("Data type: ",array.dtype)
    print("Min/Mean/Max: ", np.min(array),np.mean(array),np.max(array))
    print("\n")
    if returnYorN == "Y":
        return array

if type(args.file) == str:
    with rasterio.open(args.file,"r") as obj:
        printInfos(obj,"")

if type(args.folder) == str:
    os.chdir(args.folder)
    for f in os.listdir(args.folder):
        if f.endswith(args.endsWith):
            with rasterio.open(f,"r") as obj:
                printInfos(obj,"")

if type(args.mask) == str:
    with rasterio.open(args.mask,"r") as obj:
        array = printInfos(obj,"Y")
        #Values to remove from Mask
        for value in [0,1,2,3,8,9,10]:
            array = ma.masked_values(array, value)
        #Create Plot
        plt.figure()
        plt.title("Mask")
        ax = plt.imshow(array)        #beschreibt subplot aber nicht axis
        plt.colorbar()
        plt.show()

print("Done.")