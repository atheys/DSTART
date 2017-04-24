"""
GrowthMonitor Module.

@author: Andreas Theys.
@version: 1.0
"""

"""
Module imports.
"""
from math import e
import GridCreator as GC

"""
Exponential distribution function.

@param:  [x]     value (float; 0<=x<=1).
@param:  [lamb]  lambda-factor (float).
@return: [value] CDF-value (float).
"""
def exp(x,lamb):
    x,lamb = float(x),float(lamb)
    value = 1.-e**(-lamb*x)
    return value

"""
Root function.

@param:  [x]     value (float; 0<=x<=1).
@param:  [root]  root exponent (float).
@return: [value] root value (float).
"""
def root(x,root):
    x,root = float(x),float(root)
    value = x**(root)
    return value

"""
Weibull distribution function.

@param:  [x]     value (float; 0<=x<=1).
@param:  [lamb]  lambda-factor (float).
@param:  [k]     factor exponent (float).
@return: [value] CDF-value (float).
"""
def weibull(x,lamb,k):
    x,lamb,k = float(x),float(lamb),float(k)
    value = 1.-e**(-(x/lamb)**k)
    return value

"""
Computes exponential growth line.

@param:  [grid]   computation module grid (3D string list).
@param:  [lamb]   exponential lambda-factor (float).
@return: [limits] limit numbers list (list).
"""
def expGrowthLine(grid,lamb):
    M,N = len(grid),len(grid[0])
    lamb,limits = float(lamb),[]
    for i in range(1,M+1):
        x = float(i)/float(M)
        limits.append(int(round(float(N)*exp(x,lamb))))
    return limits

"""
Computes root growth line.

@param:  [grid]   computation module grid (3D string list).
@param:  [root]   root factor (float).
@return: [limits] limit numbers list (list).
"""
def rootGrowthLine(grid,r):
    M,N = len(grid),len(grid[0])
    r,limits = float(r),[]
    for i in range(1,M+1):
        x = float(i)/float(M)
        limits.append(int(round(float(N)*root(x,r))))
    return limits

"""
Computes Weibull growth line.

@param:  [grid]   computation module grid (3D string list).
@param:  [root]   root factor (float).
@return: [limits] limit numbers list (list).
"""
def weibullGrowthLine(grid,lamb,k):
    M,N = len(grid),len(grid[0])
    lamb,k,limits = float(lamb),float(k),[]
    for i in range(1,M+1):
        x = float(i)/float(M)
        limits.append(int(round(float(N)*weibull(x,lamb,k))))
    return limits

grid = GC.makeGrid(100.,5.,0.11)
line = rootGrowthLine(grid,0.65)
print line