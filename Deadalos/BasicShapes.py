"""
BasicsShapes Module.

@author: Andreas Theys.
@version: 1.0
"""

"""
Module imports.
"""
from math import sqrt,pi

"""
Point Object Class.
"""
class Point(object):
    
    """
    Basic Constructor.
    
    @param: [x] x-coordinate (int/float).
    @param: [y] y-coordinate (int/float).
    @param: [z] z-coordinate (int/float).
    """
    def __init__(self,x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.type = 'Point'
        return
    
    """
    Computes distance of the Point-Object to
    the origin.
    
    @return: [d] distance to the origin (float).
    """
    def odist(self):
        d = sqrt(self.x**2+self.y**2+self.z**2)
        return d
        
    """
    Computes distance of the Point-Object to
    the given Point-Object.
    
    @param:  [point] Point-Object (Point).
    @return: [d]     distance to the given Point (float).
    """   
    def dist(self,point):
        dx = (self.x-point.x)**2
        dy = (self.y-point.y)**2
        dz = (self.z-point.z)**2
        d = sqrt(dx+dy+dz)
        return d
    
    """
    Translates the Point-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """
    def translate(self,vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        return
    
    """
    Tells if Object is of the type Point.
    
    @param: [string] type string (string).
    @return: evaluation boolean.
    """
    def typ(self,string):
        if string == "Point" or string == "point":
            return True
        return False

"""
Line Object Class.
"""     
class Line(object):
    
    """
    Basic Constructor.
    
    @param: [begin] begin point of the Line-Object (Point).
    @param: [end]   end point of the Line-Object (Point).
    """
    def __init__(self,begin,end):
        self.pO = begin
        self.p1 = end
        self.type = 'Line'
        return
        
    """
    Calculates length of the Line-Object.
    
    @return: [l] length of the Line-Object (float).
    """    
    def length(self):
        l = self.p0.dist(self.p1)
        return l
    
    """
    Translates the Line-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """    
    def translate(self,vector):
        self.p0.translate(vector)
        self.p1.translate(vector)
        return
    
    """
    Tells if Object is of the type Line.
    
    @param: [string] type string (string).
    @return: evaluation boolean.
    """
    def typ(self,string):
        if string == "Line" or string == "line":
            return True
        return False

"""
Sphere Object Class.
"""
class Sphere(object):

    """
    Basic Constructor.
    
    @param: [origin] origin point of the sphere (Point).
    @param: [radius] radius of the sphere (float).
    """
    def __init__(self,origin,radius):
        self.o = origin
        self.r = float(radius)
        self.type = 'Sphere'
        return
    
    """
    Translates the Sphere-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """ 
    def translate(self,vector):
        self.o.translate(vector)
        return
        
    """
    Calculates volume of the sphere.
    
    @return: [V] volume of the sphere.
    """    
    def volume(self):
        r = self.r
        V = (4./3.)*(r**3)*pi
        return V
    
    """
    Calculates area of the sphere.
    
    @return: [A] area of the sphere.
    """    
    def area(self):
        r = self.r
        A = 4.*(r**2)*pi
        return A 
    
    """
    Tells if Object is of the type Sphere.
    
    @param: [string] type string (string).
    @return: evaluation boolean.
    """
    def typ(self,string):
        if string == "Sphere" or string == "sphere":
            return True
        return False

"""
Cylinder Object Class.
"""
class Cylinder(object):
    
    """
    Basic Constructor.
    
    @param: [origin] origin point of the cylinder (Point).
    @param: [radius] radius of the cylinder (float).
    @param: [height] height of the cylinder (float).
    """
    def __init__(self,origin,radius,height):
        self.o = origin
        self.r = float(radius)
        self.h = float(height)
        self.type = 'Cylinder'
        return
    
        """
    Translates the Cylinder-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """ 
    def translate(self,vector):
        self.o.translate(vector)
        return
    
    """
    Calculates volume of the cylinder.
    
    @return: [V] volume of the cylinder.
    """    
    def volume(self):
        r,h = self.r,self.h
        V = (r**2)*pi*h
        return V
    
    """
    Calculates area of the cylinder.
    
    @return: [A] area of the cylinder.
    """    
    def area(self):
        r,h = self.r,self.h
        A = 2.*pi*(r**2+r*h)
        return A
    
    """
    Tells if Object is of the type Cylinder.
    
    @param: [string] type string (string).
    @return: evaluation boolean.
    """
    def typ(self,string):
        if string == "Cylinder" or string == "cylinder":
            return True
        return False
    
"""
Cube Object Class.
"""
class Cube(object):
    
    """
    Basic Constructor.
    
    @param: [origin] origin point of the cube (Point).
    @param: [rib]    rib of the cube (float).
    """
    def __init__(self,origin,rib):
        self.o = origin
        self.r = float(rib)
        self.type = 'Cube'
        return
    
    """
    Translates the Cube-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """ 
    def translate(self,vector):
        self.o.translate(vector)
        return
    
    """
    Calculates volume of the cube.
    
    @return: [V] volume of the cube.
    """    
    def volume(self):
        r = self.r
        V = (r**3)
        return V
    
    """
    Calculates area of the cube.
    
    @return: [A] area of the cube.
    """    
    def area(self):
        r = self.r
        A = 6.*(r**2)
        return A
    
    """
    Tells if Object is of the type Cube.
    
    @param: [string] type string (string).
    @return: evaluation boolean.
    """
    def typ(self,string):
        if string == "Cube" or string == "cube":
            return True
        return False
    
    """
    Render Rhino cube.
    
    @param: [color] color string (string).
    """
    def toRhino(self,color='b'):
        import RhinoEngine as RE
        RE.renderCube(self.o,self.r,color)
        return

"""
Cuboid Object Class.
"""
class Cuboid(object):
    
    """
    Basic Constructor.
    
    @param: [origin] origin point of the cuboid (Point).
    @param: [length] length of the cuboid (float).
    @param: [width]  width of the cuboid (float).
    @param: [height] height of the cuboid (float).
    """
    def __init__(self,origin,length,width,height):
        self.o = origin
        self.l = float(length)
        self.w = float(width)
        self.h = float(height)
        self.type = 'Cuboid'
        return
    
    """
    Translates the Cuboid-Object using a given vector.
    
    @param: [vector] translation vector (Point).
    """ 
    def translate(self,vector):
        self.o.translate(vector)
        return
    
    """
    Calculates volume of the cuboid.
    
    @return: [V] volume of the cuboid.
    """    
    def volume(self):
        l,w,h = self.l,self.w,self.h
        V = l*w*h
        return V
    
    """
    Calculates area of the cuboid.
    
    @return: [A] area of the cuboid.
    """    
    def area(self):
        l,w,h = self.l,self.w,self.h
        A = 2.*(l*w+w*h+h*l)
        return A
    
    """
    Tells if Object is of the type Point.
    
    @param: [string] type string (string).
    @return: evaluation boolean.
    """
    def typ(self,string):
        if string == "Cuboid" or string == "cuboid":
            return True
        return False