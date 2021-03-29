# uebung6_eigenfeatures.py using scipy.spatial and own fuctions for covariance matrix

# MODULS
import argparse
import re
import math
import scipy.spatial as scispat
import numpy as np
import numpy.linalg as LA

# FUNCTIONS
# functions for covariance matrix, eigenvalue, eigenvector calculation
# (c) Magnus Bremer 2019
#Datapath: D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_small.txt
#activate rs
#python D:\_Programmieren\repos\skripts\VU_Fernerk\Abgaben\slope.py -infile D:\_Programmieren\VU_Automatisierung_Daten\Daten\pointcloud1_smaller.txt -outfile D:\_Programmieren\VU_Automatisierung_Daten\Daten\slope.txt -x 0 -y 1 -z 2 -delimiter \t -searchrad 1.0



def getCovarianceMatrix(PointArray):
    F_mean = np.mean(PointArray,axis=0)
    CovMat = np.matrix([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
    for P in PointArray:
        CovMat[0,0]+= ((P[0] - F_mean[0])**2)
        CovMat[0,1]+= (P[0] - F_mean[0])*(P[1] - F_mean[1])
        CovMat[0,2]+= (P[0] - F_mean[0])*(P[2] - F_mean[2])

        CovMat[1,0]+= (P[0] - F_mean[0])*(P[1] - F_mean[1])
        CovMat[1,1]+= ((P[1] - F_mean[1])**2)
        CovMat[1,2]+= (P[1] - F_mean[1])*(P[2] - F_mean[2])

        CovMat[2,0]+= (P[0] - F_mean[0])*(P[2] - F_mean[2])
        CovMat[2,1]+= (P[1] - F_mean[1])*(P[2] - F_mean[2])
        CovMat[2,2]+= ((P[2] - F_mean[2])**2)
    return CovMat

def GetEigenInfos(CovMat):
	# get eigenvalues and eigenvectors
	eigenvalues_unsorted,eigenvectors_unsorted = np.linalg.eig(CovMat)
	
	# sort eigenvalues and eigenvectors
	idx = eigenvalues_unsorted.argsort()[::-1]   
	eigenvalues = eigenvalues_unsorted[idx]
	eigenvectors = eigenvectors_unsorted[:,idx]
	
	# write out and reformat values
	eL = eigenvalues[0]
	eI = eigenvalues[1]
	eS = eigenvalues[2]
	evecL = np.array(eigenvectors[:,0].T)
	evecI = np.array(eigenvectors[:,1].T)
	evecS = np.array(eigenvectors[:,2].T)
	return eL,eI,eS,evecL[0],evecI[0],evecS[0] #modified

#PARSER

#definition
parser = argparse.ArgumentParser(description='this script calculates 3 eigen features using KD-tree.')
parser.add_argument('-infile', type=str, help='input file')
parser.add_argument('-outfile', type=str, help='output file')
parser.add_argument('-x', type=int, default=0, help='position of x-coordinate')
parser.add_argument('-y', type=int, default=1, help='position of y-coordinate')
parser.add_argument('-z', type=int, default=2, help='position of z-coordinate')
parser.add_argument('-delimiter', type=str, default=" ", help='delimiter symbol used when spliting columns in infile')
parser.add_argument('-searchrad', type=float, default=1.0, help='search radius for 3D neighborhood search')

#parsing
args = parser.parse_args()

#recall of variables
print (args.infile)
print (args.outfile)
print (args.x)
print (args.y)
print (args.z)
print (args.delimiter)
print (args.searchrad)


# MAIN PROGRAMM

# read file
myfile = [] 
fobj  = open(args.infile, "r") # open infile for reading
fobj_out = open(args.outfile, "w") # open outfile for writing

coordlist3d=[]
print("reading file...")
for line in fobj:
    line = line.strip() # remove newline symbol
    getrennte_linie = re.split(args.delimiter, line)
    
    # get coordinate values for x,y,z
    x = float(getrennte_linie[args.x])
    y = float(getrennte_linie[args.y])
    z = float(getrennte_linie[args.z])

    coordlist3d.append([x,y,z]) #store coordinate triples back to list

#build 3D KD search tree
pts3d = np.array(coordlist3d) #convert xyz-coordinate list of all points into array
tree3d = scispat.cKDTree(pts3d) #generate 3D KD search tree for points
c = 0
#iterate over all points and get nearest neighbors within search radius

print("calculating...")
for point in pts3d:
    searchpt3d = point  #3D search point with x,y,z
    
    # index list of neiboring points
    indexlist = tree3d.query_ball_point(searchpt3d,args.searchrad)
    
    # collect all neighboring points coordinates in new array
    neighborcoords=[]
    for i in indexlist:
        neighborpoint = pts3d[i]
        neighborcoords.append(neighborpoint)
    
    
    #ADD HERE CODE FOR EIGENFEATURES CALCULATION
    covMatrix = getCovarianceMatrix(np.array(neighborcoords))
    eigenPara = GetEigenInfos(covMatrix)
    # eiL = eigenPara[0]
    # eiI = eigenPara[1]
    #eiS = eigenPara [2]
    # evecL = eigenPara[3]
    # evecI = eigenPara[4]
    evecS = eigenPara[5]
    # linearity = (eiL - eiI)/eiL
    # planarity = (eiI-eiS)/eiL
    # sphericity = eiS/eiL 

    #ADD here code for slope calcluation
    #Idea: Angle between lower eiS and eiS, with the second vektor having set the z value to zero.

    eiSSpur = np.array([evecS[0],evecS[1],0])

    inner = np.inner(evecS,eiSSpur)
    norms = LA.norm(evecS)*LA.norm(eiSSpur)
    
    cos = inner/norms
    rad = np.arccos(np.clip(cos,-1.0,1.0))
    try:
        deg = np.rad2deg(rad)
    except:
        print("Could not deg",cos,rad)
    
    # Umwandlung der Liste in einen String
    searchpt = searchpt3d.astype(str) #cast array as string, with nice floating point formatting
    outstring = '%s,%s,%s,%.2f,%.2f,%.2f' % (searchpt3d[0],searchpt3d[1],searchpt3d[2],cos,rad,deg)
    
    # Datei schreiben
    myline = outstring+"\n"
    fobj_out.write(myline)
    
    #Optional, in order to check 
    # print(evecS,eiSSpur,inner,norms,cos,rad,deg)
    # c+= 1
    # if c == 10:
    #     break
#print(eiS,evecS)
# Fileobjekte schließen
fobj.close()
fobj_out.close()

print("done.")