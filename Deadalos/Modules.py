"""
Modules Module.
@author: Andreas Theys.
@version: 1.3
"""

"""
Module imports.
"""
from ComplexShapes import TruncOctahedron as Toc

"""
Life Support Module Object Class.
"""
class LifeSupport(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'L'
        self.r = (1./3.)*self.R
        self.color = 'g'
        self.mod = Toc(self.c,self.R)
        return

"""
Habitation Module Object Class.
"""
class Habitation(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'H'
        self.r = (1./3.)*self.R
        self.color = 'b'
        self.mod = Toc(self.c,self.R)
        return

"""
Manufacturing Module Object Class.
"""
class Manufacturing(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'M'
        self.r = (1./3.)*self.R
        self.color = 'r'
        self.mod = Toc(self.c,self.R)
        return

"""
Manufacturing Module Object Class.
"""
class Processing(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'P'
        self.r = (1./3.)*self.R
        self.color = 'o'
        self.mod = Toc(self.c,self.R)
        return

"""
Storage Module Object Class.
"""
class Storage(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'St'
        self.r = (1./3.)*self.R
        self.color = 'y'
        self.mod = Toc(self.c,self.R)
        return

"""
Shielding Module Object Class.
"""
class Shielding(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'Sh'
        self.r = (1./3.)*self.R
        self.color = ' '
        self.mod = Toc(self.c,self.R)
        return
    
"""
Telemetry Module Object Class.

@note: currently redundant.
"""
class Telemetry(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'T'
        self.r = (1./3.)*self.R
        self.color = 'k'
        self.mod = Toc(self.c,self.R)
        return