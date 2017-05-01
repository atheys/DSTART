"""
Materials module.

@author: Andreas Theys.
@version: 1.0
"""

"""
Module imports.
"""
from random import random as rdn

"""
Material Object Class.
"""
class Material(object):
    
    """
    Basic Constructor.
    
    @param: [symbol]  material symbol (string).
    @param: [name]    material name (string).
    @param: [color]   color string (string).
    @param: [density] material density (float).
    @param: [young]   Young's modulus (float; GPa).
    @param: [yiel]    yield stress (float; MPa).
    @param: [crit]    critical stress (float; MPa).  
    """
    def __init__(self,symbol,name,color,density,young,yiel,crit):
        self.symbol = str(symbol)
        self.name = str(name)
        self.color = str(color)
        self.dens = float(density)
        self.young = float(young)
        self.yiel = float(yiel)
        self.crit = float(crit)

"""
Component Object Class.
"""
class Component(object):
    
    """
    Basic Constructor.
    
    @param: [material] relevant material (Material).
    @param: [perc]     percentage (float).
    """
    def __init__(self,material,perc):
        self.material = material
        self.perc = float(perc)

"""
Normalization function.

@param:  [components]  list of components (Component-list).
@return: [components] list of normalized components (Component-list).
"""
def normalize(components):
    new,s = [],0.
    for comp in components:
        if comp.perc > 0.:
            new.append(comp)
            s += comp.perc
    for comp in new:
        comp.perc /= s
    return new

"""
Computes (cumulative) percentages list.

@param:  [components]  list of components (Component-list).
@return: [p]           list of cumulative percentages (list of floats).
"""
def percentages(components):
    s = 0.
    p = [s]
    for comp in components:
        s += comp.perc
        p.append(s)
    return p   

"""
Composition Object Class.
"""
class Composition(object):
    
    """
    Basic Constructor.
    
    @param: [components] components [Component-list].
    """
    def __init__(self,components):
        self.components = normalize(components)
        self.p = percentages(components)  
    
    """
    Selects (randomly) a material in the composition.
    """
    def select(self):
        q = rdn()
        for i in range(len(self.p)-1):
            if self.p[i]<=q and q<self.p[i+1]:
                return self.components[i].material
        return Material('UL','Useless','k',0.,0.,0.,0.)