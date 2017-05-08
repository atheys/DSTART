"""
Materials Module.

@author: Andreas Theys.
@version: 1.0
"""

"""
Module imports.
"""
from MaterialMaker import Material

"""
Compositions.
"""
al_2024 = [('Al',0.94),('Cu',0.04),('Mg',0.015),('Mn',0.005)]
al_7075 = [('Al',0.9055),('Zn',0.055),('Mg',0.025),('Cu',0.015),('Cr',0.2)]
al_honey = [('Al',0.9855),('Cu',0.002),('Mg',0.005),('Mn',0.005),('Zn',0.0025)] 
alsteel = [('Fe',0.965),('Si',0.02),('Mn',0.009),('C',0.006)]
ni_foam = [('Ni',0.95),('Al',0.05)]
cu_foam = [('Cu',1.)]
al_foam = [('Al',0.927),('Si',0.07),('Mg',0.003)]
cuag_foam = [('Cu',0.75),('Ag',0.25)]
wcco = [('W',0.47),('C',0.47),('Co',0.06)]
albe = [('Al',0.38),('Be',0.595),('Ni',0.025)]
alsic = [('Al',0.75),('Si',0.125),('C',0.125)]
wcomp = [('W',0.95),('Ni',0.025),('Cu',0.025)]
wcu = [('W',0.8),('Cu',0.2)]
cfiber = [('C',1.)]
ti1 = [('Ti',0.89),('Al',0.07),('Mo',0.04)]
ti2 = [('Ti',0.89),('Al',0.045),('Mo',0.04),('Si',0.005),('Sn',0.02)]
ni1 = [('Ni',0.7),('Cr',0.2),('Fe',0.07),('Ti',0.025),('Al',0.005)]
ni2 = [('Ni',0.37),('Cr',0.21),('Co',0.33),('Mo',0.09)]
cu_alloy = [('Cu',0.98),('Ni',0.02)]
sic = [('Si',0.5),('C',0.5)]

"""
Aluminium.
"""
Al_2024 = Material('Aluminium 2024',al_2024,2780.,25000.)
Al_7075 = Material('Alumnium 7075',al_7075,2800.,27000.)

"""
Titanium.
"""
Ti_1 = Material('Titanium',ti1,4480.,35000.)                            # Titanium Ti-7Al-4Mo, STA
Ti_2 = Material('Titanium',ti2,4600.,30000.)                            # TIMET TIMETAL 550 (Ti-4Al-4Mo-2Sn) Titanium Alloy Solution Treated

"""
Nickel.
"""
Ni_1 = Material('Nickel',ni1,8240.,12500.)                              # ATI Allvac Nickelvac X- 751 UNS N07751 Nickel Superalloy
Ni_2 = Material('Nickel Alloy',ni2,8430.,50000.)                        # Carpenter MP35N* Ni-Co-Cr-Mo Alloy, 65% Cold Reduction

"""
Copper.
"""
Cu_alloy = Material('Copper Alloy',cu_alloy,8780.,17500.)               # Copper-Nickel-Phosphorus-Tellurium alloy, UNS C19100  

"""
Steel.
"""
AlSteel = Material('Alloy Steel',alsteel,7850.,25000.)

"""
Other metals.
"""
WCCo = Material('Tungsten Carbide/Cobalt',wcco,14950.,22500.)
AlBe = Material('Aluminium Berylium Composite',albe,2170.,15000.)       # Materion AlBeCast IC910 Aluminum Beryllium Composite
AlSiC = Material('Aluminium Berylium Composite',alsic,2880.,24000.)     # Materion AMC225XE T4 Aluminum/Silicon Carbide MMC Forged Plate
WCu = Material('Tungsten Copper Composite',wcu,15100.,4500.)            # Hogen Duralloy H30W 80 Tungsten/20 Copper PM Metal Composite
W_comp = Material('Tungsten Composite',wcomp,18000.,5000.)              # H.C. Starck HPM 1801 Tungsten High Density Composite
SiC = Material('Silicon Carbide',sic,3100.,100000.)                     # Silicon Carbide, Alpha SiC

"""
Foams.
"""
Ni_foam = Material('Nickel Foam',ni_foam,280.,6000.)                    # FiberNide Nickel Aluminide Foam Atomic 10% Aluminum
Cu_foam = Material('Copper Foam',cu_foam,500.,7800.)
Al_foam = Material('Aluminium Foam',al_foam,400.,7800.)                 # Cymat A35620SC 040SS Stabilized Aluminum Foam
CuAg_foam = Material('Copper-Aluminium Foam',cuag_foam,600.,7500.)

"""
Honeycombs.
"""
Al_honey = Material('Aluminium Honeycomb',al_honey,40.,10800.)

"""
Carbon Fiber.
"""
C_fiber = Material('Carbon Fiber',cfiber,1800.,225000.)                 # Hexcel UHM Carbon Fiber (12,000 Filaments)