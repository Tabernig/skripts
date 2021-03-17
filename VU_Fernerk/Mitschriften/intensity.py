#intensity.py

#MODULE
import argparse

#Parser
#Definition
parser = argparse.ArgumentParser(description="this skript removes outliers")
parser.add_argument("-infile",type=str,help="input file") #es wird eine variable im file definiert
parser.add_argument("-outfile",type=str,help="output file")
parser.add_argument("-delimiter",type=str,help="delimiter symbol used when splitting columns of infile")
parser.add_argument("-colno",type=int,default=4,help="column number indicating column containing intensity values")
parser.add_argument("-threshold",type=float,default=255,help="outliers larger than threshold are removed")


#Übergabe der argumente an das skript

args= parser.parse_args()

# Aufruf
print(args.infile)
print(args.outfile)
print(args.delimiter)
print(args.colno)
print(args.threshold)


#Hauptprogramm


print("Done")

#D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt
