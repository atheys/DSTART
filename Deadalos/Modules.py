"""
Modules Module.
@author: Andreas Theys.
@version: 1.5
"""

"""
Module imports.
"""
from ComplexShapes import TruncOctahedron as Toc


class Habitation(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'Hab'
        self.r = (1./3.)*self.R
        self.color = 'y'
        self.mod = Toc(self.c,self.R)
        return

class LifeSupport(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'LSup'
        self.r = (1./3.)*self.R
        self.color = 'g'
        self.mod = Toc(self.c,self.R)
        return

class Mining(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'Pros'
        self.r = (1./3.)*self.R
        self.color = 'o'
        self.mod = Toc(self.c,self.R)
        return

class Processing(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'Pros'
        self.r = (1./3.)*self.R
        self.color = 'o'
        self.mod = Toc(self.c,self.R)
        return

class Manufacturing(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'Man'
        self.r = (1./3.)*self.R
        self.color = 'r'
        self.mod = Toc(self.c,self.R)
        return
        
class OreStorage(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'OStore'
        self.r = (1./3.)*self.R
        self.color = 'y'
        self.mod = Toc(self.c,self.R)
        return

class RefinedStorage(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'RStore'
        self.r = (1./3.)*self.R
        self.color = 'y'
        self.mod = Toc(self.c,self.R)
        return

class RadShielding(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'RadSh'
        self.r = (1./3.)*self.R
        self.color = ' '
        self.mod = Toc(self.c,self.R)
        return

class ColShielding(object):
    
    """
    Basic Constructor.
    
    @param: [center] center point of the module (Point).
    @param: [R]      rib (length) of the module (int/float).
    """
    def __init__(self,center,R):
        self.c = center
        self.R = float(R)
        self.label = 'ColSh'
        self.r = (1./3.)*self.R
        self.color = ' '
        self.mod = Toc(self.c,self.R)
        return
    
class Thrust(object):
    
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