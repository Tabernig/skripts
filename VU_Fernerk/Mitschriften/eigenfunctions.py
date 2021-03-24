# functions for covariance matrix, eigenvalue, eigenvector calculation
# (c) Magnus Bremer 2019

import numpy as np
import scipy.spatial
from math import *

########################################################
####             Functions                ##############
########################################################

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
	return eL/eL,eI/eL,eS/eL,evecL[0],evecI[0],evecS[0]





	
	







    
    



    
