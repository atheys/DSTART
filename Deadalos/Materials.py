"""
Materials Module.

@author: Andreas Theys.
@version: 1.0
"""

"""
Module imports.
"""
from MaterialMaker import Material,g_copper,mu_air

"""
Compositions.
"""
al_2024 = [('Al',1.)]
al_honey = [('Al',1.)] 
alsteel = [('Fe',0.965),('Si',0.02),('C',0.006)]
ni_foam = [('Ni',0.95),('Al',0.05)]
cu_foam = [('Cu',1.)]
al_foam = [('Al',1.)]
cuag_foam = [('Cu',0.75),('Ag',0.25)]
alsic = [('Al',0.75),('Si',0.125),('C',0.125)]
wcomp = [('W',0.95)]
wcu = [('W',0.8),('Cu',0.2)]
cfiber = [('C',1.)]
ti1 = [('Ti',1.)]
ni1 = [('Ni',0.7),('Fe',0.3)]
cu_alloy = [('Cu',0.98),('Ni',0.02)]
sic = [('Si',0.5),('C',0.5)]

"""
Aluminium.
"""
Al_2024 = Material('Aluminium 2024',al_2024,2780.,25000.,3.5*10.**7,1.256665*10.**(-6))

"""
Titanium.
"""
Ti_1 = Material('Titanium',ti1,4480.,35000.,2.38*10.**6,1.00005*mu_air)                            # Titanium Ti-7Al-4Mo, STA

"""
Nickel.
"""
Ni_1 = Material('Nickel',ni1,8240.,12500.,1.43*10.**7,4.9*10.**(-4))                              # ATI Allvac Nickelvac X- 751 UNS N07751 Nickel Superalloy

"""
Copper.
"""
Cu_alloy = Material('Copper Alloy',cu_alloy,8780.,17500.,g_copper,1.256629*10.**(-6))               # Copper-Nickel-Phosphorus-Tellurium alloy, UNS C19100  

"""
Steel.
"""
AlSteel = Material('Alloy Steel',alsteel,7850.,25000.,1.45*10.**6,1.26*10.**(-4))

"""
Other metals.
"""
AlSiC = Material('Aluminium Silicium Carbide',alsic,2880.,24000.,1.11111*10.**5,0.999*mu_air)     # Materion AMC225XE T4 Aluminum/Silicon Carbide MMC Forged Plate
WCu = Material('Tungsten Copper Composite',wcu,15100.,4500.,2.63157*10.**5,1.9*mu_air)            # Hogen Duralloy H30W 80 Tungsten/20 Copper PM Metal Composite
W_comp = Material('Tungsten Composite',wcomp,18000.,5000.,9.0909*10.**4,1.05*mu_air)      # H.C. Starck HPM 1801 Tungsten High Density Composite
SiC = Material('Silicon Carbide',sic,3100.,100000.,0.625*10.**3,0.9999936*mu_air)                     # Silicon Carbide, Alpha SiC

"""
Foams.
"""
Ni_foam = Material('Nickel Foam',ni_foam,280.,6000.,1.43*10.**7,4.9*10.**(-4))                    # FiberNide Nickel Aluminide Foam Atomic 10% Aluminum
Cu_foam = Material('Copper Foam',cu_foam,500.,7800.,g_copper,1.256629*10.**(-6))
Al_foam = Material('Aluminium Foam',al_foam,400.,7800.,3.5*10.**7,1.256665*10.**(-6))                 # Cymat A35620SC 040SS Stabilized Aluminum Foam
CuAg_foam = Material('Copper-Silver Foam',cuag_foam,600.,7500.,6.045*10.**7,1.25662473217*10.**(-6))

"""
Honeycombs.
"""
Al_honey = Material('Aluminium Honeycomb',al_honey,40.,10800.,3.5*10.**7,1.256665*10.**(-6),False)

"""
Carbon Fiber.
"""
C_fiber = Material('Carbon Fiber',cfiber,1800.,225000.,19342.3597679,mu_air,False) # Hexcel UHM Carbon Fiber (12,000 Filaments)