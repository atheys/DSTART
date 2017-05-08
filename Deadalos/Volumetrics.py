"""
Volumetrics Module.

@author: Andreas Theys.
@version: 1.2
"""

"""
Module imports.
"""
from math import sqrt
from Composition import space

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


"""
V = 0.3*10**8                   # m/s
dens = 1.*10**6               # mol/m^3
energy = 18.75*1.6022*10**(-13)   # J

E_col = V*dens*energy
rho = 1800.                     # kg/m^3 
E_s = 250000.                     # J/kg

MR = 36.
f_i = 0.15
a = 5.
manu = 24.*3600.
A = (6.+12.*sqrt(3))*(a**2)

V = (E_col*A*manu)/(rho*E_s-MR*(1./f_i)*A*E_col)
t = V/(24.*sqrt(2)*a**2)
print rho*E_s
print MR*(1./f_i)*A*E_col
print t
"""