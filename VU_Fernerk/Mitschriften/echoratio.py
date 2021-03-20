#echoratio.py

#Calculates nearest neighbour for each point


#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Mitschriften\echoratio.py -infile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointsDis.txt -x 0 -y 1 -z 2 -delimiter \t -searchradius 1.0


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
for line in fobj:
    line = line.strip()
    getrennte_Line = re.split(args.delimiter,line)
    x= float(getrennte_Line[args.x])
    y= float(getrennte_Line[args.y])
    z= float(getrennte_Line[args.z])

    coordlist.append([x,y,z])
pts3D = np.array(coordlist)
tree3d = spatial.cKDTree(pts3D)

mindist = 99999
maxdist = 0
neigandis = []
for point in pts3D:
    searchpt = point
    #indexlist = tree3d.query_ball_point(searchpt,args.searchradius)
    while True:
        dd,ii = tree3d.query(point,k=3)
        distances = dd.tolist()
        distanceR = []
        xt = 0
        for value in distances:
            if (float(value) > 0) and (float(value) <= args.searchradius):
                distanceR.append(value)
                break
            xt += 1
        break
    if len(ii) <= xt:
        nearestpoint = -99999
    else:
        #print(ii,len(ii),xt)
        nearestpoint = pts3D[ii[xt]]
        if distanceR[0] > maxdist:
            maxdist = distanceR[0]
        if distanceR[0] < mindist:
            mindist = distanceR[0]
    
    point=point.tolist()
    if type(nearestpoint) == int:
         nearestpoint=[nearestpoint]
    else:
        nearestpoint=nearestpoint.tolist()
    neigandis.append(point)
    neigandis.append(nearestpoint)
    neigandis.append(distanceR)

print(point,type(point), nearestpoint,type(nearestpoint) ,distanceR,type(distanceR))
neighbourArray = np.array(neigandis)
print(neighbourArray)
print("min",str(mindist))
print("max",str(maxdist))

#Fileobjekte schließen
fobj.close()
fobj_Out.close()
print("done.")