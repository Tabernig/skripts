#intensity.py

#MODULE
import argparse
import re
import numpy as np

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

#Datei Einlesen
fobj = open(args.infile,"r")        #Eingabefile im Lesemodus
fobj_Out = open(args.outfile,"w")   #Ausgabefile im Schreibmodus öffnen



#Spalten aufteilen
myfile = []
count = 0 #fehlerhafte punkte
for line in fobj:
    line= line.strip() #entfernen des Zeilenumbruchs
    getrennte_Line = re.split(args.delimiter,line)
    colidx = args.colno - 1 #Umwaltung der Spaltennummer in Index
    intensity = getrennte_Line.pop(colidx)
    if float(intensity) <= args.threshold:  #Intensitätswerte > Schwellenwert entfernen
        getrennte_Line.insert(colidx,str(intensity)) #passende Intensitätswerte werden in Line an ursprünglicher Position wieder eingefügt
        outstring = ",".join(getrennte_Line) #Umwandlung der Liste in einen String
        outstring = outstring +"\n"
        fobj_Out.write(outstring) #Datei schreiben
    else:
        count += 1

print(count)


fobj.close()
fobj_Out.close()

print("Done")

#Standard Input
#D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt
#D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small_corrected.txt
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Mitschriften\intensity.py -infile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small_corrected.txt -delimiter \t -colno 4 -threshold 255