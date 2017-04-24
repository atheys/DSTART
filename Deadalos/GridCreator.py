"""
GridCreator Module.

@author: Andreas Theys.
@version: 1.2
"""

"""
Module imports.
"""
from math import sqrt,floor,tan,radians
from BasicShapes import Point as P

"""
Determines nearest even number.

@param:  [k] relevant number (int).
@return:     nearest even number.
"""
def nearestEvenNumber(k):
    k = int(k)
    if k%2 == 0:
        return k-1
    return k

"""
Determines N-coefficient for number y- and z-cells.

@param:  [D] largest internal circular diameter (float/m).
@param:  [r] (uniform) rib length of the modules (float/m).
@return: [N] N-coefficient (int).
"""
def N(D,r):
    D,r = float(D),float(r)
    coeff = (sqrt(2.)*D)/(2.8*r)
    N = nearestEvenNumber(int(floor(coeff)))
    return N

"""
Determines M-coefficient for number x-cells.

@param:  [D]   largest internal circular diameter (float/m).
@param:  [r]   (uniform) rib length of the modules (float/m).
@param:  [phi] collision safety angle (float/radians).
@return: [M]   M-coefficient (int).
"""
def M(D,r,phi):
    D,r,phi = float(D),float(r),min(float(phi),radians(9.736))
    if phi <= 0.:
        return -1
    else:
        coeff = ((2.*(1.-tan(phi))-sqrt(2.))/(2.8*tan(phi)*r))*D
        M = nearestEvenNumber(int(floor(coeff)))
        return M

"""
Makes 3D grid matrix.

@param:  [D]    largest internal circular diameter (float/m).
@param:  [r]    (uniform) rib length of the modules (float/m).
@param:  [phi]  collision safety angle (float/radians).
@return: [grid] grid matrix (3D list strings).
"""      
def makeGrid(D,r,phi):
    n,m = N(D,r),M(D,r,phi)
    row = n*['']
    matrix,grid = [],[]
    for i in range(n):
        matrix.append(row)
    for i in range(m):
        grid.append(matrix)
    return grid

"""
Makes 3D grid matrix.

@param:  [D]    largest internal circular diameter (float/m).
@param:  [r]    (uniform) rib length of the modules (float/m).
@param:  [phi]  collision safety angle (float/radians).
@return: [grid] grid point matrix (3D list Point-Objects).
"""      
def makePointGrid(D,r,phi):
    D,r,phi = float(D),float(r),min(float(phi),radians(9.736))
    n,m,r2 = N(D,r),M(D,r,phi),(1./3.)*r
    h,w,C = 0.25*sqrt(2.)*(r-r2),0.25*(r+r2),(n-1)/2
    pgrid = []
    for i in range(m):
        temp1 = []
        for j in range(n):
            temp2 = []
            for k in range(n):
                dj,dk = C-j,k-C
                x,y,z = 2.*float(i)*w,2.*float(dk)*w,0.
                if i%2==0:
                    if dk%2==0:
                        z+= 4.*dj*h
                    else:
                        z+= 4.*dj*h+2.*h
                else:
                    if dk%2==0:
                        z+= 4.*dj*h+2.*h
                    else:
                        z+= 4.*dj*h
                temp2.append(P(x,y,z))
            temp1.append(temp2)
        pgrid.append(temp1)
    return pgrid