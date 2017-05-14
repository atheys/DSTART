"""
GrowthMonitor Module.

@author: Andreas Theys.
@version: 2.0
"""
  
"""
Decreasing growth line function.

@param:  [x]     value (float; 0<=x<=1).
@return: [value] line value (float).
"""  
def decrease(x):
    value = 1.-float(x)
    return value

"""
Computes exponential growth line.

@param:  [grid]   computation module grid (3D string list).
@param:  [lamb]   exponential lambda-factor (float).
@return: [limits] limit numbers list (list).
"""
def decreasingGrowthLine(grid):
    M,limits = len(grid),[]
    for i in range(1,M+1):
        x = float(i)/float(M)
        limits.append(decrease(x))
    return limits