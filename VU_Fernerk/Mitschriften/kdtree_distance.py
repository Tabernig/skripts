#echoratio.py

#Calculates nearest neighbour for each point


#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_smaller.txt
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Mitschriften\kdtree_distance.py -infile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_smaller.txt -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointsDis.txt -x 0 -y 1 -z 2 -delimiter \t -searchradius 1.0


#MODULE
import argparse
import re
import numpy as np
import scipy.spatial as scispat
import math

#PARSER
parser = argparse.ArgumentParser(description="this skript calculates the distance between two nearest points")
parser.add_argument("-infile",type=str,help="Input file")
parser.add_argument("-outfile",type=str,help="Output file")
parser.add_argument("-delimiter",type=str,help="delimiter splitting columns")
parser.add_argument("-x",type=int,help="index of column containing X coordinates")
parser.add_argument("-y",type=int,help="index of column containing Y coordinates")
parser.add_argument("-z",type=int,help="index of column containing Z coordinates")
parser.add_argument("-searchradius",type=float,default=1.0,help="search radius")

args = parser.parse_args()

# Aufruf
print(args.infile)
print(args.outfile)
print(args.delimiter)
print(args.x)
print(args.y)
print(args.z)
print(args.delimiter)
print(args.searchradius)
#HAUPTPROGRAMM
fobj = open(args.infile,"r")
fobj_Out = open(args.outfile,"w")


coordlist = []

#File Einlesen
for line in fobj:
    line = line.strip()
    getrennte_Line = re.split(args.delimiter,line)

    #Koordinaten Extrahieren
    x= float(getrennte_Line[args.x])
    y= float(getrennte_Line[args.y])
    z= float(getrennte_Line[args.z])

    coordlist.append([x,y,z])


pts3D = np.array(coordlist)
tree3d = scispat.cKDTree(pts3D) #Erzeugen von 3D KD Suchbaum


mindist = 99999
maxdist = 0
neigandis = []
for searchpt in pts3D:
    indexlist = tree3d.query_ball_point(searchpt,args.searchradius)
    x1,y1,z1 = searchpt[0],searchpt[1],searchpt[2]  #Koordinaten des Searchpoints

    #Berechnung der Distanzen zum Suchradius
    distanzen = []
    for i in indexlist:
        poitinsearchrad = pts3D[i]
        x2,y2,z2 = poitinsearchrad[0],poitinsearchrad[1],poitinsearchrad[2] #Koordinaten des Nachbarn i
        dist = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
        distanzen.append(dist)
    
    #Finden der Minimumdistanz
    if len(distanzen)==1:
        index0dist = distanzen.index(0.0)
        distanzen.insert(index0dist,99999)
    else:
        distanzen.remove(0.0)
        mindist = min(distanzen)

    # Outputfile schreiben
    searchpt = searchpt.astype(str)
    outstring = "%s,%s,%s, %.2f" %(searchpt[0],searchpt[1],searchpt[2],mindist)
    myline = outstring + "\n"
    fobj_Out.write(myline)

#Fileobjekte schließen
fobj.close()
fobj_Out.close()
print("done.")