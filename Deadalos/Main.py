
from ComplexShapes import TruncOctahedron as TO
from BasicShapes import Point as P
from GridCreator import filled,mined,updateGrid,neighbors,makeGrid,makeStarshipBooleanGrid,makePointGrid,makeAsteroidBooleanGrid
from random import random as rdn
from sets import Set

D = 500.
rl = 15.
theta = 0.2
#point = P(0.,0.,0.)
#octa1 = TO(point,z).toRhino('xyz','b')

grid = makeGrid(D,rl,theta)
M,N1,N2 = len(grid),len(grid[0]),len(grid[0][0])
ssgrid = makeStarshipBooleanGrid(D,rl,theta)
pgrid = makePointGrid(D,rl,theta)
agrid = makeAsteroidBooleanGrid(D,rl,theta)
colors = ['r','b','g','y']
n = len(colors)-1
colors2 = ['gray',' ',' ',' ']
n2 = len(colors2)-1

for i in range(len(grid)):
    for j in range(len(grid[i])):
        for k in range(len(grid[i][j])):
            if agrid[i][j][k]:
                TO(pgrid[i][j][k],rl).toRhino(colors2[int(round(n2*rdn()))])
"""               
ugrid = updateGrid(grid,agrid,ssgrid)
begin = (int(N2),int(round(N1/2)),int(round(N2/2)))
bound = [begin]
X,k = 0,len(bound)-1
while X>0 and len(bound)>0:
    node = bound[int(round(rdn()*k))]
    i,j,k = int(node[0]),int(node[1]),int(node[2])    
    TO(pgrid[i][j][k],rl).toRhino(colors[int(round(n*rdn()))],'xyz')
    filled(node,'random',ugrid,ssgrid)
    bound.remove(node)
    bound = list(Set(bound)|Set(neighbors(node,ugrid,True)[0]))
    k,X = len(bound)-1,X-1"""


    

