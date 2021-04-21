# implementierung von region growing
#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small_shift.las
#activate rs
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Abgaben\segment.py -infile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small_shift.las -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\segment.las

# MODULS
import os
import numpy as np
import pclpy



#definition
a_infile = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small_shift.las"
a_outfile = "D:\_Programmieren\VU_Automatisierung_Daten\Daten\\test2"
a_format = "PointXYZI"
a_searchrad = 2.0 #help=search radius for 3D neighborhood search for normal estimation
a_numpts = 30     #help='region growing number of neighboring points')
a_minsize =20     #help='region growing minimum number of points in segment')
a_maxsize = 10000 #help='region growing maximum number of points in segment')
a_smooth = 0.5    #help='region growing smoothing threshold (min. angle between normals)')
a_curvature = 5.0 #help='region growing curvature threshold')
a_residual = 10.0 #help='region growing residual threshold')

# MAIN PROGRAMM

pts = pclpy.read_las(a_infile, a_format)

#Compute Normal Vectors

normals = pts.compute_normals(radius = a_searchrad)

#region growing segmentation  -  returns PointIndices



a_outfile+= ".las" 
segments = pts.region_growing(normals, n_neighbours=a_numpts, min_size=a_minsize, max_size=a_maxsize, smooth_threshold=a_smooth, curvature_threshold=a_curvature, residual_threshold=a_residual)

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
        print(id)
print(len(segments))

#Anzahl der Elemente Pro Segment
print(len(segments[segid].indices))
#write pointcloud file

pclpy.write_las(pts,a_outfile,a_format)




print("done.")