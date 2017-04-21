"""
Modules Module.
@author: Andreas Theys.
@version: 1.0
"""

"""
Module imports.
"""
from ComplexShapes import TruncOctahedron as Toc

"""
Life support (L) = 1 --> Green
Habitation (H) = 2 --> Blue
Manufacturing (M) = 3
Storage (St) = 4
Shielding (Sh) = 5
Telemetry/Communications (Tc) = 6
"""

class LifeSupport(object):
    
    def __init__(R):
        self.R = float(R)
        self.r = (1./3.)*self.R
        self.color = 'g'
        self
        
        