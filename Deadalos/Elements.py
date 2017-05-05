"""
Materials module.

@author: Andreas Theys.
@version: 1.0
"""

"""
Material Object Class.
"""
class Isotope(object):
    
    """
    Basic Constructor.
    
    @param: [symbol]    material symbol (string).
    @param: [name]      material name (string).
    @param: [color]     color string (string).
    @param: [amu_rho]   atomic mass units or desnity (float).
    @param: [E_s]       specific energy absorption (float;J/kg).
    @param: [protons]   number of protons.
    @param: [neutrons]  number of neutrons.
    @param: [electrons] number of electrons.
    """
    def __init__(self,symbol,name,color,amu_rho,protons=0.,neutrons=0.,electrons=0.):
        self.symbol = str(symbol)
        self.name = str(name)
        self.color = str(color)
        self.amu_rho = float(amu_rho)
        self.protons = float(protons)
        self.neutrons = float(neutrons)
        self.electrons = float(electrons)
        self.type = "Isotope"
        return

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
        self.type = "Component"
        return

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
    def __init__(self,components,rho=0.,E_s=0.):
        self.components = normalize(components)
        self.p = percentages(components)
        self.rho = float(rho)
        self.E_s = float(E_s)
        self.type = "Composition"
        return