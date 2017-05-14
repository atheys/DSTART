"""
MaterialMaker Module.

@author: Andreas Theys.
@version: 1.0
"""

"""
Module imports.
"""
from Elements import Component,Composition
from Composition import elements

"""
Material Object Class.
"""
class Material(object):
    
    """
    Basic constructor.
    
    @param: [name] name of material (str).
    @param: [comp] composition of elements (nested list of tuples/dict).
    @param: [rho]  composition of elements (float; kg/m^3).
    @param: [E_s]  specific energy absorption (float;J/kg).
    @param: [iso]  isotropic material property (bool).
    """
    def __init__(self,name,comp,rho=0.,E_s=0.,iso=True):
        self.name = str(name)
        self.rho = float(rho)
        self.E_s = float(E_s)
        self.iso = bool(iso) 
        approve,comps = True,[]
        if type(comp) is list:
            comp = dict(comp)
        if type(comp) is dict:
            for item in comp.keys():
                try:
                    temp = Component(elements[item],comp[item])
                    comps.append(temp)
                except Exception:
                    approve = False
        if approve:
            self.composition = Composition(comps,self.rho,self.E_s)
        else: 
            print "Wrong input!"
        return 

"""
Normalization function.

@param:  [composition] composition percentage list (list).
@return: [composition] normalized composition percentage list (list).
"""
def normalize(composition):
    s = 0.
    for item in composition:
        s += float(item)
    for item in composition:
        item /= s
    return composition
    
"""
Creates composite material.

@param: [name]        name of the compositie material (str).
@param: [composition] percentage composition of the materials (list).
@param: [materials]   materials list (list).
@param: [iso]         isotropic material property (bool).
@param: [c]           composite material (Material).
"""
def composite(name,composition,materials):
        name,composition = str(name),normalize(composition)
        N = len(composition)
        if len(materials) == N:
            rho,E_s,isotropic = 0.,0.,True
            elements = dict([])
            for i in range(N):
                rho += composition[i]*materials[i].rho
                E_s += composition[i]*materials[i].E_s
                isotropic = isotropic and materials[i].iso
                for el in materials[i].composition.components:
                    sym = el.material.components[0].material.symbol
                    p = composition[i]*el.perc
                    try:
                        elements[sym] += p
                    except Exception:
                        elements[sym] = p
        c = Material(name,elements,rho,E_s,isotropic)
        return c