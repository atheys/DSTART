
"""
Module imports.
"""
from math import sqrt,floor
from BasicShapes import Point as P
import RhinoEngine as RE
import GridCreator as GC

"""
Determines nearest even number.

@param:  [k] relevant number (int).
@return:     nearest even number.
"""
def nearestEvenNumber(k):
    k = int(k)
    if k%2 == 0:
        return k
    return k-1

"""
Creates abstract grid point list.

@param:  [R]  asteroid radius (float).
@param:  [Z]  cube rib length (float).
@return: [ag] abstract grid (int list).
"""
def abstractGrid(R,Z):
    R,Z = float(R),float(Z)
    R = sqrt(R**2-0.25*Z**2)
    N,k = int(floor(R/Z)),-1
    if N%2==1:
        k = -2
    ag,temp = [],[]
    for i in range(0,N):
        n = nearestEvenNumber(int(floor(sqrt(i*Z*(2*R-i*Z))/Z)))
        ag.append(n)
        temp.append(n)
    for i in range(len(temp)+k,-1,-1):
        ag.append(temp[i])
    return ag
  
"""
Makes a square matrix.

@param:  [n]      number of rows/columns (int).
@return: [matrix] square matrix (2D boolean list).
"""  
def makeMatrix(n):
    n,matrix = int(n),[]
    for i in range(n):
        matrix.append(n*[False])
    return matrix

"""
Creates boolean grid.

@param:  [R]  asteroid radius (float).
@param:  [Z]  cube rib length (float).
@return: [bg] boolean grid (2D boolean list).
"""
def booleanGrid(R,Z):
    R,Z = float(R),float(Z)
    ag,bg = abstractGrid(R,Z),[]
    for n in ag:
        bg.append(makeMatrix(n))
    return bg
    
"""
Shapes boolean matrix.

@param:  [matrix] initial boolean matrix (2D boolean list).
@return: [matrix] shape boolean matrix (2D boolean list).
"""    
def shape(matrix):
    N = len(matrix)
    C = N/2
    if N%2 == 0:
        for i in range(N):
            for j in range(N):
                l1,l2 = C-i,(C-j)
                if i<C:
                    l1-=1
                if j<C:
                    l2-=1
                eval1 = sqrt(l1**2+l2**2)<=float(N)/2.
                eval2 = i==C or i==(C-1)
                eval3 = j==C or j==(C-1)
                if eval1 or eval2 or eval3:
                    matrix[i][j] = True        
    else:
        for i in range(N):
            for j in range(N):
                eval1 = sqrt((float(abs(C-i))+0.5)**2 \
                +(float(abs(C-j))+0.5)**2)<=float(N)/2.
                eval2 = i==C 
                eval3 = j==C
                if eval1 or eval2 or eval3:
                    matrix[i][j] = True 
    return matrix

"""
Builds asteroid grid.

@param:  [R]  asteroid radius (float).
@param:  [Z]  cube rib length (float).
@return: [ag] asteroid boolean grid (3D boolean list).
"""
def asteriodGrid(R,Z):
    R,Z = float(R),float(Z)
    bg,ag = booleanGrid(R,Z),[] 
    for item in bg:
        ag.append(shape(item))
    return ag
    
"""
Builds asteroid point grid.

@param:  [R]   asteroid radius (float).
@param:  [Z]   cube rib length (float).
@return: [apg] asteroid point grid (3D Point list).
"""    
def asteroidPointGrid(R,Z):
    R,Z = float(R),float(Z)
    bg,apg = booleanGrid(R,Z),[] 
    for i in range(len(bg)):
        temp1,x = [],-(0.5+i)*Z
        N = len(bg[i])
        C = N/2
        for i in range(N):
            temp2 = []
            for j in range(N):
                y,z = 0.,0.
                if N%2 == 0:
                    y,z = 0.5*Z+(j-C)*Z,0.5*Z+(C-i)*Z
                else:
                    y,z = (j-C)*Z,(C-i)*Z
                temp2.append(P(x,y,z))
            temp1.append(temp2)
        apg.append(temp1)
    return apg