#kdtree_distance.py

#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Mitschriften\distancebetweenallpoints-SLOW.py -infile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointsDis.txt -x 0 -y 1 -z 2 -delimiter \t -searchradius 1.0


#MODULE
import argparse
import re
import numpy as np
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


count = 1
limit =1000
coordlist = []
for line in fobj:
    if count<limit:
        line = line.strip()
        getrennte_Line = re.split(args.delimiter,line)
        x= float(getrennte_Line[args.x])
        y= float(getrennte_Line[args.y])
        z= float(getrennte_Line[args.z])

        coordlist.append([count,x,y,z])
        count+=1

eleCount = 0
for xyz in coordlist:
    x1, y1, z1= xyz[1],xyz[2],xyz[3]
    for elements in coordlist:
        x2,y2,z2=elements[1],elements[2],elements[3]
        if x1==x2 and y1==y2 and z1 == z2:
            pass
        else: 
            dist = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
            #print("Distanz zwischen Punkt "+str(xyz[0])+"und Punkt "+str(elements[0])+"is: "+str(dist))
            
        eleCount += 1
        # if eleCount%100 == 0:
        #     print(str(eleCount/100))

#print(eleCount)
pts3D = np.array(coordlist)

print(pts3D)
#Fileobjekte schließen
fobj.close()
fobj_Out.close()
print("done.")