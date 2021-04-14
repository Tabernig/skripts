# implementierung von region growing
#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small_shift.las
#activate rs
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Abgaben\segment.py -infile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small_shift.las -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\segment.las

# MODULS
import os
import argparse
import numpy as np
import pclpy


# PARSER

#definition
parser = argparse.ArgumentParser(description='this script segments a 3d point cloud.')
parser.add_argument('-infile', type=str, help='input file in las-format')
parser.add_argument('-outfile', type=str, help='output file')
parser.add_argument('-format', type=str, default="PointXYZI", help='format of infile and outfile strucutre, e.g. PointXYZI')
parser.add_argument('-searchrad', type=float, default=2.0, help='search radius for 3D neighborhood search for normal estimation')
parser.add_argument('-numpts', type=int, default=30, help='region growing number of neighboring points')
parser.add_argument('-minsize', type=int, default=20, help='region growing minimum number of points in segment')
parser.add_argument('-maxsize', type=int, default=10000, help='region growing maximum number of points in segment')
parser.add_argument('-smooth', type=float, default=0.5, help='region growing smoothing threshold (min. angle between normals)')
parser.add_argument('-curvature', type=float, default=5.0, help='region growing curvature threshold')
parser.add_argument('-residual', type=float, default=10.0, help='region growing residual threshold')

#parsing
args = parser.parse_args()

#recall of variables
print (args.infile)
print (args.outfile)
print (args.format)
print (args.searchrad)
print (args.numpts)
print (args.minsize)
print (args.maxsize)
print (args.smooth)
print (args.curvature)
print (args.residual)


# MAIN PROGRAMM

pts = pclpy.read_las(args.infile, args.format)

#Compute Normal Vectors

normals = pts.compute_normals(radius = args.searchrad)

#region growing segmentation  -  returns PointIndices

segments = pts.region_growing(normals, n_neighbours=args.numpts, min_size=args.minsize, max_size=args.maxsize, smooth_threshold=args.smooth, curvature_threshold=args.curvature, residual_threshold=args.residual)

# store segment ID as intensity attribute

# iterate over segments
for segid in range(0,len(segments)):
    for i in range(0,len(segments[segid].indices)):
        # get point ID
        pointid = segments[segid].indices[i]
        
        #print(segid,len(segments[segid].indices),pointid)
        #scale segment ID to 16 bit
        id = 65536.0/len(segments)*segid

        pts.points[pointid].intensity = id

#write pointcloud file

pclpy.write_las(pts,args.outfile,args.format)




print("done.")