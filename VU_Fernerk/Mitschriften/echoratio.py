#echoratio.py

#Calculates nearest neighbour for each point


#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Mitschriften\echoratio.py -infile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\echoratio.txt -x 0 -y 1 -z 2 -delimiter \t -searchradius 1.0


#MODULE
import argparse
import re
import numpy as np
from scipy import spatial
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
coord2d = []
echoAr = []
for line in fobj:
    line = line.strip()
    getrennte_Line = re.split(args.delimiter,line)
    x= float(getrennte_Line[args.x])
    y= float(getrennte_Line[args.y])
    z= float(getrennte_Line[args.z])
    coordlist.append([x,y,z])
    coord2d.append([x,y])
    echoAr.append([x,y,z,0])
pts3D = np.array(coordlist)
pts2D = np.array(coord2d)
echoAr = np.array(echoAr)
tree3d = spatial.cKDTree(pts3D)
tree2d = spatial.cKDTree(pts2D)

index = 0
nr2d=[]

for searchpt in pts2D:
    indexlist = tree2d.query_ball_point(searchpt,args.searchradius)
    nr2d.append(len(indexlist))


for searchpt in pts3D:
    indexlist = tree3d.query_ball_point(searchpt,args.searchradius)
    nr3d = len(indexlist)
    a = searchpt
    echoratio = nr3d/nr2d[index]*100
    a= np.append(a,[echoratio])
    echoAr[index] = a
    a = a.tolist()
    outstring = ",".join(getrennte_Line) #Umwandlung der Liste in einen String
    outstring = outstring +"\n"
    # for value in a:
    fobj_Out.write(str(a)) #Datei schreiben
print(a,type(a))


    




#print(echoAr)
#3d Distanze 

#Fileobjekte schließen
fobj.close()
fobj_Out.close()
print("done.")