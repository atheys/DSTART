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

"""
Determines area of a module exposed to outer spce medium.

@param: [a]     rib length of the modules (float).
@param: [sides] inclusive indicator (list of int).
@param: [A]     exposed area (float).
"""
def area(a,sides):
    a,A = float(a),0.
    # Edge cases
    if len(sides) == 14:
        return (6.+12.*sqrt(3))*(a**2)
    if len(sides) == 0:
        return A
    if 1 in sides:
        A += a**2
    if 2 in sides:
        A += 1.5*sqrt(3)*a**2
    if 3 in sides:
        A += 1.5*sqrt(3)*a**2
    if 4 in sides:
        A += 1.5*sqrt(3)*a**2
    if 5 in sides:
        A += 1.5*sqrt(3)*a**2
    if 6 in sides:
        A += a**2
    if 7 in sides:
        A += a**2
    if 8 in sides:
        A += a**2
    if 9 in sides:
        A += a**2
    if 10 in sides:
        A += 1.5*sqrt(3)*a**2
    if 11 in sides:
        A += 1.5*sqrt(3)*a**2
    if 12 in sides:
        A += 1.5*sqrt(3)*a**2
    if 13 in sides:
        A += 1.5*sqrt(3)*a**2
    if 14 in sides:
        A += a**2
    return A

def uniformWeights(n):
    n,w = int(n),[]
    for i in range(n):
        w.append(1./float(n))
    return w

def determineK(material,storage,V):
    m,V = 0.,float(V)
    for element in material.composition.components:
        sym = element.material.components[0].material.symbol
        f_el_mat = element.perc
        f_el = asteroid_components[sym].perc
        try:
            V_el = float(storage[sym])
        except Exception:
            V_el = 0.
        K_el = max(f_el_mat-V_el/V,0.)/f_el
        if K_el>m:
            m = K_el
    return m
        

def performance(material,storage,V):
    V = float(V)
    K = determineK(material,storage,V)
    if K>0.:
        return (material.E_s*material.rho)/(K**(0.75))
    else:
        return material.E_s*material.rho


def partials(weights,materials,storage,V,prec=0.000001):
    V,partial = float(V),[]
    comp0 = composite(' ',weights,materials)
    perf0 = performance(comp0,storage,V)
    for i in range(len(weights)):
        temp = weights[i]
        weights[i] += prec
        comp1 = composite(' ',weights,materials)
        perf1 = performance(comp1,storage,V)
        partial.append((perf1-perf0)/prec)
        weights[i] = temp
    return partial
        

def deepAscent(materials,storage,V,prec=0.000001,n=10):
    k = len(materials)
    w = np.array(uniformWeights(k))
    x_0,F_0 = np.array(k*[0.]),np.array(k*[0.])
    gamma = 1.
    while n>0 and abs(gamma)>prec:
        part = np.array(partials(w,materials,storage,V))
        part /= np.linalg.norm(part)
        gamma = (w-x_0)*(part-F_0)
        gamma /= np.linalg.norm(part-F_0)**2
        gamma = sum(gamma)
        x_0,F_0 = w,part
        w = w+gamma*part
        w /= sum(w)
        n-=1
    return w.tolist()


def determineComposite(materials,storage,V,prec=0.000001,n=10):
    if len(materials)==1:
        w = [1.]
        comp = composite('Material',w,materials)
    else:
        w = deepAscent(materials,storage,V,prec,n)
        comp = composite('Material',w,materials)
    return w,comp

def modThickness(a,sides,sigma,manu,MR,particles,materials,storage,prec=0.000001,n=10,energy=energy_units(avgMass()),frac=0.1):
    a,sigma,manu,MR,particles = float(a),float(sigma),float(manu),1./float(MR),float(particles)
    E_col,A,V = collisionEnergy(particles,energy,frac),area(a,sides),12.*sqrt(2)*a**2
    w,composite = determineComposite(materials,storage,V,prec,n)
    rho,SEA,K = composite.rho,composite.E_s,determineK(composite,storage,V)
    for i in range(2):
        print sigma*E_col*A*manu
        print rho*SEA
        print A*E_col*MR*K
        t = (sigma*E_col*manu)/((rho*SEA-A*E_col*MR*K))
        V = 8.*sqrt(2)*(3.*a**2*t-3.*a*t**2+t**3)
        w,composite = determineComposite(materials,storage,V,prec,n)
        rho,SEA,K = composite.rho,composite.E_s,determineK(composite,storage,V)
        print w,V,t
        print


from Materials import Cu_foam,C_fiber,SiC

a = 5.
sides = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
sigma = 2.
manu = 30.*24.*3600.
MR = 1./1800.
particles = 0.5*10**6
materials = [C_fiber,Cu_foam,SiC]
storage = dict([])
modThickness(a,sides,sigma,manu,MR,particles,materials,storage)