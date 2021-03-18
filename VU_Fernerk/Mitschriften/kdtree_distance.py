#kdtree_distance.py

#Calculates nearest neighbour for each point


#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Mitschriften\kdtree_distance.py -infile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointsDis.txt -x 0 -y 1 -z 2 -delimiter \t -searchradius 1.0


#MODULE
import argparse
import re
import numpy as np
from scipy import spatial

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
for line in fobj:
    line = line.strip()
    getrennte_Line = re.split(args.delimiter,line)
    x= float(getrennte_Line[args.x])
    y= float(getrennte_Line[args.y])
    z= float(getrennte_Line[args.z])

    coordlist.append([x,y,z])
pts3D = np.array(coordlist)
tree3d = spatial.cKDTree(pts3D)

pointndNeighbour = []
for point in pts3D:
    searchpt = point
    indexlist = tree3d.query_ball_point(searchpt,5)
    nearestpoint = pts3D[indexlist[0]]
    pointndNeighbour.append([point,nearestpoint])

neighbourArray = np.array(pointndNeighbour)

print(neighbourArray)
#Fileobjekte schließen
fobj.close()
fobj_Out.close()
print("done.")