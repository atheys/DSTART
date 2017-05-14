"""
GridCreator Module.

@author: Andreas Theys.
@version: 1.4
"""

"""
Module imports.
"""
from math import sqrt,floor,tan
from BasicShapes import Point as P
import GrowthMonitor as GM

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
    coeff = D/r
    N1 = nearestUnevenNumber(int(floor(coeff)))
    N2 = nearestUnevenNumber(int(floor(1.5*float(N1))))
    return N1,N2

"""
Determines M-coefficient for number x-cells.

@param:  [D]   largest internal circular diameter (float/m).
@param:  [r]   (uniform) rib length of the modules (float/m).
@param:  [phi] collision safety angle (float/radians).
@return: [M]   M-coefficient (int).
"""
def M(D,r,phi):
    D,r,phi = float(D),float(r),float(phi)
    if phi <= 0.:
        return -1
    else:
        coeff = (0.75*D)/(tan(phi)*r)
        M = int(floor(coeff))
        return M

"""
Makes 3D grid matrix.

@param:  [D]    largest internal circular diameter (float/m).
@param:  [r]    (uniform) rib length of the modules (float/m).
@param:  [phi]  collision safety angle (float/radians).
@return: [grid] grid matrix (3D list strings).
"""      
def makeGrid(D,r,phi):
    n1,n2 = N(D,r)
    m = M(D,r,phi)
    row = n2*['']
    matrix,grid = [],[]
    for i in range(n1):
        matrix.append(row)
    for i in range(m+n2/2):
        grid.append(matrix)
    return grid

"""
Makes 3D Starship boolean grid matrix.

@param:  [D]    largest internal circular diameter (float/m).
@param:  [r]    (uniform) rib length of the modules (float/m).
@param:  [phi]  collision safety angle (float/radians).
@return: [grid] boolean grid matrix (3D list strings).
"""  
def makeStarshipBooleanGrid(D,r,phi):
    D,r,phi = float(D),float(r),float(phi)
    grid = makeGrid(D,r,phi)
    M,N1,N2 = len(grid),len(grid[0]),len(grid[0][0])
    limits = GM.decreasingGrowthLine(grid)
    mid1,mid2,bgrid = N1/2,N2/2,[]
    for i in range(M):
        temp1 = []
        r = limits[i]
        for j in range(N1):
            temp2 = []
            for k in range(N2):
                r1,r2 = 2.*float(j-mid1)/float(N1),2.*float(k-mid2)/float(N2)
                r3 = 2.*float(i-mid2)/float(N2)
                e1,e2,e3 = bool(r1**2+r2**2<=r**2),r1**2+r2**2+r3**2>1.,i>mid2
                e = bool(e1 and e2 and e3)
                temp2.append(e)
            temp1.append(temp2)
        bgrid.append(temp1)       
    return bgrid  
    
"""
Makes 3D Asteroid boolean grid matrix.

@param:  [D]    largest internal circular diameter (float/m).
@param:  [r]    (uniform) rib length of the modules (float/m).
@param:  [phi]  collision safety angle (float/radians).
@return: [grid] boolean grid matrix (3D list strings).
"""  
def makeAsteroidBooleanGrid(D,r,phi):
    D,r,phi = float(D),float(r),float(phi)
    grid = makeGrid(D,r,phi)
    M,N1,N2 = len(grid),len(grid[0]),len(grid[0][0])
    limits = GM.decreasingGrowthLine(grid)
    mid1,mid2,bgrid = N1/2,N2/2,[]
    for i in range(M):
        temp1 = []
        r = limits[i]
        for j in range(N1):
            temp2 = []
            for k in range(N2):
                r1,r2 = 2.*float(j-mid1)/float(N1),2.*float(k-mid2)/float(N2)
                r3 = 2.*float(i-mid2)/float(N2)
                e = bool(r1**2+r2**2+r3**2<=1.)
                temp2.append(e)
            temp1.append(temp2)
        bgrid.append(temp1)       
    return bgrid 

"""
Makes 3D grid matrix.

@param:  [D]    largest internal circular diameter (float/m).
@param:  [r]    (uniform) rib length of the modules (float/m).
@param:  [phi]  collision safety angle (float/radians).
@return: [pgrid] grid point matrix (3D list Point-Objects).
"""      
def makePointGrid(D,r,phi):
    D,r,phi = float(D),float(r),float(phi)
    grid = makeGrid(D,r,phi)
    M,N1,N2 = len(grid),len(grid[0]),len(grid[0][0])
    r2 = r/3.
    h,w,C = 0.25*sqrt(2.)*(r-r2),0.25*(r+r2),(N2-1)/2
    pgrid = []
    for i in range(M):
        temp1 = []
        for j in range(N1):
            temp2 = []
            for k in range(N2):
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

def updateGrid(grid,agrid,sgrid):
    ugrid = []
    for i in range(len(grid)):
        temp1 = []
        for j in range(len(grid[i])):
            temp2 = []
            for k in range(len(grid[i][j])):
                if agrid[i][j][k]:
                    temp2.append('Asteroid')
                elif not(sgrid[i][j][k]):
                    temp2.append('Edge')
                else:
                    temp2.append('')
            temp1.append(temp2)
        ugrid.append(temp1)
    return ugrid

def mined(n,grid,agrid):
    i,j,k = n[0],n[1],n[2]
    if agrid[i][j][k]:
        grid[i][j][k] = ''
        agrid[i][j][k] = False
    return
    
def filled(n,symbol,grid,sgrid):
    i,j,k = int(n[0]),int(n[1]),int(n[2])
    if sgrid[i][j][k]:
        grid[i][j][k] = str(symbol)
        sgrid[i][j][k] = False
    return
    
   
"""
Determines all neighboring nodes of certain grid point.

@param:  [n]      grid coordinate point (tuple).
@param:  [grid]   grid matrix (3D nested list of strings).
@return: [actual] actual list of neighboring nodes (list of tuples).
"""   
def neighbors(n,grid,filled=False):
    i,j,k = int(n[0]),int(n[1]),int(n[2])
    nodes = [ (i,j-1,k),(i+1,j,k),(i,j,k+1),(i-1,j,k),(i,j,k-1),\
              (i+1,j,k-1),(i+1,j,k+1),(i-1,j,k+1),(i-1,j,k-1),\
              (i+1,j+1,k),(i,j+1,k+1),(i-1,j+1,k),(i,j+1,k-1),(i,j+1,k)]
    actual,numbers = [],[]
    for l in range(len(nodes)): 
        node = nodes[l]
        try:
            x,y,z = node[0],node[1],node[2]
            b = bool(grid[x][y][z] == '')
            if x>=0 and y>=0 and z>=0:
                if filled:
                    if b: 
                        actual.append(node)
                        numbers.append(l+1)
                else:
                    actual.append(node)
                    numbers.append(l+1)  
        except Exception:
            print 'OOPS'
    return actual,numbers

"""
Helper method to find node in done list.

@param:  [n]    node specification (tuple mixture).
@param:  [done] done-list (list of done nodes).
@return:        evaluation boolean (bool).
"""
def foundInDone(n,done):
    for item in done:
        if item[0]==n:
            return True
    return False

"""
Finds nodes in active list.

@param:  [n]    node specification (tuple mixture).
@param:  [V]    node list (list).
@return:        node (tuple mixture or None-object).
"""
def findNode(n,V):
    for item in V:
        if item[0]==n:
            return item
    return None

"""
Finds shortest distance node.

@param:  [V] node list (list).
@return: [n] shortest distance node (tuple mixture or None-object).
"""
def findMinNode(V):
    m,n = 1000000.,None
    for item in V:
        if item[1]<m:
            n = item
            m = item[1]
    return n
    
"""
Finds shortest path from one module to another.

@param: [n1] first node/module (tuple).
@param: [n2] second node/module (tuple).
@return:     number of modules to cross (float).
"""   
def Dijkstra(n1,n2,grid):
    # Initiation
    V = [(n1,0.)]
    current = findMinNode(V)
    V.remove(current)
    done = []
    # Iteration
    while current[0] != n2 and current != None:
        d = current[1]
        N ,numbers = neighbors(current[0],grid,True)
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
    # Termination
    if current == None:
        return -1.
    else:
        return current[1]