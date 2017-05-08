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
def nearestUnevenNumber(k):
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
    N = nearestUnevenNumber(int(floor(coeff)))
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
        M = nearestUnevenNumber(int(floor(coeff)))
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
   
"""
Determines all neighboring nodes of certain grid point.

@param:  [n]      grid coordinate point (tuple).
@param:  [grid]   grid matrix (3D nested list of strings).
@return: [actual] actual list of neighboring nodes (list of tuples).
"""   
def neighbors(n,grid,filled=False):
    i,j,k = n[0],n[1],n[2]
    nodes = [(i,j,k-1),(i+1,j,k),(i,j+1,k),(i-1,j,k),(i,j-1,k),\
             (i+1,j-1,k),(i+1,j+1,k),(i-1,j+1,k),(i-1,j-1,k),\
             (i+1,j,k+1),(i,j+1,k+1),(i-1,j,k+1),(i,j-1,k+1),(i,j,k+1)]
    actual = []
    for l in range(len(nodes)-1,-1,-1): 
        node = nodes[l]
        try:
            x,y,z = node[0],node[1],node[2]
            b = grid[x][y][z] != ''
            if x>=0 and y>=0 and z>=0:
                if filled:
                    if b: 
                        actual.append(node)
                else:
                    actual.append(node)
        except Exception:
            temp = ' '
    return actual

def foundInDone(n,done):
    for item in done:
        if item[0]==n:
            return True
    return False

def findNode(n,V):
    for item in V:
        if item[0]==n:
            return item
    return None

def findMinNode(V):
    m,n = 1000000.,None
    for item in V:
        if item[1]<m:
            n = item
            m = item[1]
    return n
    
    
def Dijkstra(n1,n2,grid):
    # Initiation
    V = [(n1,0.)]
    current = findMinNode(V)
    V.remove(current)
    done = []
    # Iteration
    while current[0] != n2 and current != None:
        d = current[1]
        N = neighbors(current[0],grid,True)
        for n in N:
            if not foundInDone(n,done):
                node = findNode(n,V)
                if node != None:
                   if node[1]>d+1.:
                       V.remove(node)
                       V.append((n,d+1.)) 
                else:
                   V.append((n,d+1.)) 
        done.append(current) 
        current = findMinNode(V)
        V.remove(current)
    if current == None:
        return -1.
    else:
        return current[1]