"""
Volumetrics Module.

@author: Andreas Theys.
@version: 1.2
"""

"""
Module imports.
"""
from math import sqrt
from Composition import space,asteroid_components
from MaterialMaker import composite
import numpy as np

"""
Module preamble constants.
"""
prot,neut = 1.67262189821/(10.**27),1.67492747121/(10.**27)
elec,amu,c = 9.1093835611/(10.**31),1.66053904/(10.**27),3.*10.**8
proton,neutron,electron = prot*c**2,neut*c**2,elec*c**2
unit = amu*c**2

"""
Computes the average atomic mass of the deep space medium.

@param:  [environment] deep space environment composition.
@return: [mass]        average atomic mass of the medium.
"""
def avgMass(environment=space):
    mass = 0.
    for element in environment.components:
        p = element.perc
        for isotope in element.material.components:
            fraction = p*isotope.perc
            mass_fraction = fraction*isotope.material.amu_rho
            mass += mass_fraction
    return mass

"""
Computes relativistic kinetic energy.

@param:  [nProt] number of protons.
@param:  [nNeut] number of neutrons.
@param:  [nElec] number of electrons.
@param:  [frac]  fraction of the speed of light.
@return: [E]     relativistic kinetic energy (J).
"""
def energy_particles(nProt,nNeut,nElec,frac=0.1):
    nProt,nNeut,nElec = float(nProt),float(nNeut),float(nElec)
    gamma = sqrt(1./(1.-frac**2))-1.
    E = nProt*proton+nNeut*neutron+nElec*electron
    E *= gamma
    return E

"""
Computes relativistic kinetic energy.

@param:  [units] number of amu's.
@param:  [frac]  fraction of the speed of light.
@return: [E]     relativistic kinetic energy (J).
"""  
def energy_units(units,frac=0.1):
    units = float(units)
    gamma = sqrt(1./(1.-frac**2))-1.
    E = units*unit
    E *= gamma
    return E

"""
Calculates the average collision energy.

@param:  [A]         surface area of the structure (m^2).
@param:  [partciles] number of particles per unit volume (particles/m^3).
@param:  [energy]    average relativistic kinetic energy (J/particle).
@param:  [frac]      fraction of the speed of light.
@return: [E_col]     collision energy coeffcient (J/(s*m^2)).
"""
def collisionEnergy(particles,energy=energy_units(avgMass()),frac=0.1):
    V = frac*c
    E_col = V*energy*particles
    return E_col

def uniformWeights(n):
    n,w = int(n),[]
    for i in range(n):
        w.append(1./float(n))
    return w

def performance(material):
    return (material.E_s*material.rho)

def partials(weights,materials,prec=0.000001):
    partial = []
    comp0 = composite(' ',weights,materials)
    perf0 = performance(comp0)
    for i in range(len(weights)):
        temp = weights[i]
        weights[i] += prec
        comp1 = composite(' ',weights,materials)
        perf1 = performance(comp1)
        partial.append((perf1-perf0)/prec)
        weights[i] = temp
    return partial
        

def deepAscent(materials,prec=0.000001,n=10):
    k = len(materials)
    w = np.array(uniformWeights(k))
    x_0,F_0 = np.array(k*[0.]),np.array(k*[0.])
    gamma = 1.
    while n>0 and abs(gamma)>prec:
        part = np.array(partials(w,materials))
        part /= np.linalg.norm(part)
        gamma = (w-x_0)*(part-F_0)
        gamma /= np.linalg.norm(part-F_0)**2
        gamma = sum(gamma)
        x_0,F_0 = w,part
        w = w+gamma*part
        w /= sum(w)
        n-=1
    return w.tolist()


def determineComposite(materials,prec=0.000001,n=10):
    if len(materials)==1:
        w = [1.]
        comp = composite('Material',w,materials)
    else:
        w = deepAscent(materials,prec,n)
        comp = composite('Material',w,materials)
    return w,comp        


def thickness(composite,E_col,time):
    E_col,time = float(E_col),float(time)
    t = (E_col*time)/(composite.E_s*composite.rho)
    return t

def length(composite,E_col,time):
    E_col,time = float(E_col),float(time)
    t = thickness(composite,E_col,time)
    return 66.5/46.5*t

def thicknessList(composite,E_col,time):
    t = thickness(composite,E_col,time)/15.5
    t_list = [ 2./3.*t,t/3.,t/3.,t/3.,2./3.*t,t/3.,t/3., \
               t/3.,t,t/2.,t/2.,t/2.,4./3.*t,2./3.*t,2./3.*t, \
               2./3.*t,4./3.*t,2./3.*t,2./3.*t,2./3.*t,3.*t]
    return t_list
    


from Materials import Al_2024,Cu_foam,C_fiber,SiC

a = 5.
sides = [2]
sigma = 1.
manu = 24.*3600.
MR = 1./50.
particles = 0.5*10**6
materials = [Al_2024,Cu_foam,C_fiber]
storage = dict([])
w,comp = determineComposite(materials,prec=0.000001,n=100)
E_col = 14.2
print thickness(comp,E_col,manu)
print thicknessList(comp,E_col,manu)
print length(comp,E_col,manu)