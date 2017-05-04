"""
ComplexShapes Module.

@author: Andreas Theys.
@version: 1.1
"""

"""
Module imports.
"""
from math import sqrt,pi

"""
Tetrahedron Object Class. 
"""
class Tetrahedron(object):
    
    """
    Basic Constructor.
    
    @param: [origin] origin point of the tetrahedron (Point).
    @param: [rib]    rib of the tetrahedron (float).
    """
    def __init__(self,origin,rib):
        self.o = origin
        self.r = float(rib)
        self.type = 'Tetrahedron'
        return
    
    """
    Translates the Tetrahedron-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """ 
    def translate(self,vector):
        self.o.translate(vector)
        return
    
    """
    Calculates volume of the tetrahedron.
    
    @return: [V] volume of the tetrahedron.
    """ 
    def volume(self):
        r = self.r
        V = (r**3)*(sqrt(2)/12.)
        return V
    
    """
    Calculates area of the tetrahedron.
    
    @return: [A] area of the tetrahedron.
    """ 
    def area(self):
        r = self.r
        A = sqrt(3)*(r**2)
        return A

"""
Octahedron Object Class. 
"""
class Octahedron(object):
    
    """
    Basic Constructor.
    
    @param: [origin] origin point of the octahedron (Point).
    @param: [rib]    rib of the octahedron (float).
    """
    def __init__(self,origin,rib):
        self.o = origin
        self.r = float(rib)
        self.type = 'Octahedron'
        return
    
    """
    Translates the Octahedron-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """ 
    def translate(self,vector):
        self.o.translate(vector)
        return
    
    """
    Calculates volume of the octahedron.
    
    @return: [V] volume of the octrahedron.
    """ 
    def volume(self):
        r = self.r
        V = (r**3)*(sqrt(2)/3.)
        return V
    
    """
    Calculates area of the octahedron.
    
    @return: [A] area of the octahedron.
    """ 
    def area(self):
        r = self.r
        A = 2.*sqrt(3)*(r**2)
        return A

"""
Truncated Octahedron Object Class. 
"""
class TruncOctahedron(object):
    
    """
    Basic Constructor.
    
    @param: [origin] origin point of the truncated octahedron (Point).
    @param: [rib]    rib of the truncated octahedron (float).
    """
    def __init__(self,origin,rib):
        self.o = origin
        self.r = float(rib)
        self.r2 = (1./3.)*float(rib)
        self.type = 'TruncOctahedron'
        return
    
    """
    Translates the TruncOctahedron-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """ 
    def translate(self,vector):
        self.o.translate(vector)
        return
    
    """
    Calculates volume of the octahedron.
    
    @return: [V] volume of the octrahedron.
    """ 
    def volume(self):
        r = self.r
        V = 8.*(r**3)*sqrt(2)
        return V
    
    """
    Calculates area of the octahedron.
    
    @return: [A] area of the octahedron.
    """ 
    def area(self):
        r = self.r
        A = (6.+12.*sqrt(3))*(r**2)
        return A
    
    """
    Converts figure to Rhino mesh.
    
    @param: [origin]      origin point of the figure (Point).
    @param: [orientation] orientation mode of the figure (string).
    @param: [color]       color string of the figure (string).
    """
    def toRhino(self,orientation='xyz',color=' '):
        import RhinoEngine as RE
        orien,c = orientation,color
        RE.renderTruncOctahedron(self.o,self.r,self.r2,orien,c)
        return

"""
Capsule Object Class. 
"""
class Capsule(object):
    
    """
    Basic Constructor.
    
    @param: [origin] origin point of the capsule (Point).
    @param: [radius] radius of the capsule (float).
    @param: [height] height of the capsule (float).
    """
    def __init__(self,origin,radius,height):
        self.o = origin
        self.r = float(radius)
        self.h = float(height)
        self.type = 'Capsule'
        return
    
    """
    Translates the Capsule-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """ 
    def translate(self,vector):
        self.o.translate(vector)
        return
    
    """
    Calculates volume of the capsule.
    
    @return: [V] volume of the capsule.
    """ 
    def volume(self):
        r,h = self.r,self.h
        V = (r**2)*pi*(h+(4./3.)*r)
        return V
    
    """
    Calculates area of the caspule.
    
    @return: [A] area of the capsule.
    """ 
    def area(self):
        r,h = self.r,self.h
        A = 2.*pi*r*(2.*r+h)
        return A
    
"""
Truncated Capsule Object Class. 
"""
class TruncCapsule(object):
    
    """
    Basic Constructor.
    
    @param: [origin] origin point of the capsule (Point).
    @param: [radius] radius of the capsule (float).
    @param: [height] height of the capsule (float).
    """
    def __init__(self,origin,radius,height,radius2,height2):
        self.o = origin
        self.r = float(radius)
        self.h = float(height)
        self.r2 = float(radius2)
        self.h2 = float(height2)
        self.type = 'TruncCapsule'
        return
    
    """
    Translates the Capsule-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """ 
    def translate(self,vector):
        self.o.translate(vector)
        return
    
    """
    Calculates volume of the capsule.
    
    @return: [V] volume of the capsule.
    """ 
    def volume(self):
        r,h,r2,h2 = self.r,self.h,self.r2,self.h2
        V = (r**2)*pi*h+(2./3.)*pi*h2*((r**2)+r*r2+(r2**2))
        return V
    
    """
    Calculates area of the caspule.
    
    @return: [A] area of the capsule.
    """ 
    def area(self):
        r,h,r2,h2 = self.r,self.h,self.r2,self.h2
        A_1 = pi*(r+r2)*sqrt((r-r2)**2+(h2**2))
        A_2 = (r2**2)*pi
        A = 2.*(A_1+A_2)+2.*pi*r*h
        return A