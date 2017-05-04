"""
Volumetrics Module.

@author: Andreas Theys.
@version: 1.0
"""

"""
Module imports.
"""
from math import sqrt

"""
Module preamble constants.
"""
prot,neut = 1.67262189821/(10.**27),1.67492747121/(10.**27)
elec,amu,c = 9.1093835611/(10.**31),1.66053904/(10.**27),3.*10.**8
proton,neutron,electron = prot*c**2,neut*c**2,elec*c**2
unit = amu*c**2

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