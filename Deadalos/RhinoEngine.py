"""
Engine Module.

@author: Andreas Theys.
@version: 1.1
"""

"""
Module imports.
"""
import Rhino as r
import Rhino.Geometry as geo
import scriptcontext as sc
import rhinoscriptsyntax as rs 
import System as sys
from math import sqrt

"""
Selects a color for the 

@param:  [color] color string (string).
@return:         color system attribute (sys.Drawing.color).
"""
def drawColor(color):
    if color == 'b' or color == 'blue':
        return sys.Drawing.Color.Blue
    elif color == 'r' or color == 'red':
        return sys.Drawing.Color.Red
    elif color == 'g' or color == 'green':
        return sys.Drawing.Color.Green
    elif color == 'y' or color == 'yellow':
        return sys.Drawing.Color.Yellow
    elif color == 'o' or color == 'orange':
        return sys.Drawing.Color.Orange  
    elif color == 'br' or color == 'brown':
        return sys.Drawing.Color.Brown
    elif color == 'pi' or color == 'pink':
        return sys.Drawing.Color.Pink
    elif color == 'i' or color == 'indigo':
        return sys.Drawing.Color.Indigo
    elif color == 'p' or color == 'purple':
        return sys.Drawing.Color.Purple
    elif color == 'k' or color == 'black':
        return sys.Drawing.Color.Black
    elif color == 'gr' or color == 'gray':
        return sys.Drawing.Color.Gray
    elif color == 'dgr' or color == 'darkgray':
        return sys.Drawing.Color.DarkGray 
    elif color == 'w' or color == 'white':
        return sys.Drawing.Color.White
    elif color == 's' or color == 'silver':
        return sys.Drawing.Color.Silver
    else:
        return sys.Drawing.Color.Black       

"""
Provides color in ObjectAttributes.

@param:  [color] color string (string).
@return:         color ObjectAttribute (r.DocObjects.ObjectAttribute).
"""
def giveColor(color):
    index = sc.doc.Materials.Add()
    mat = sc.doc.Materials[index]
    mat.DiffuseColor = drawColor(color)
    mat.SpecularColor = drawColor(color)
    mat.CommitChanges()
    attributes = r.DocObjects.ObjectAttributes()
    attributes.MaterialIndex = index
    attributes.MaterialSource = r.DocObjects.ObjectMaterialSource.MaterialFromObject
    return attributes

"""
Render sphere object in Rhino.

@param: [o]     object origin point (Point).
@param: [r]     object radius (int/float).
@param: [color] color string (string).
"""
def renderSphere(o,r,color='b'):
    center = geo.Point3d(o.x,o.y,o.z)
    sphere = geo.Sphere(center,r)
    attr = giveColor(color)
    sc.doc.Objects.AddSphere(sphere,attr)
    sc.doc.Views.Redraw()
    return

"""
Render cylinder object in Rhino.

@param: [o]           object origin point (Point).
@param: [r]           object radius (int/float).
@param: [h]           object height (int/float).
@param: [orientation] orientation string (string).
@param: [color]       color string (string).
"""
def renderCylinder(o,r,h,orientation='xyz',color='b'):
    c = [0.,0.,0.]
    c['xyz'.index(orientation[2])] = 0.5*h
    x_o,y_o,z_o = o.x-c[0],o.y-c[1],o.z-c[2]
    x_f,y_f,z_f = o.x+c[0],o.y+c[1],o.z+c[2]
    p_o,p_f = geo.Point3d(x_o,y_o,z_o),geo.Point3d(x_f,y_f,z_f)
    axis = p_f-p_o
    plane = geo.Plane(p_o,axis)
    circle = geo.Circle(plane,r)
    cyl = geo.Cylinder(circle,axis.Length).ToBrep(True, True)
    attr = giveColor(color)
    sc.doc.Objects.AddBrep(cyl,attr)
    sc.doc.Views.Redraw()
    return

"""
Render cube object in Rhino.

@param: [o]     object origin point (Point).
@param: [r]     object rib length (int/float).
@param: [color] color string (string).
"""
def renderCube(o,r,color='b'):
    x_o,y_o,z_o = o.x-0.5*r,o.y-0.5*r,o.z-0.5*r
    x_f,y_f,z_f = o.x+0.5*r,o.y+0.5*r,o.z+0.5*r
    p_o = geo.Point3d(x_o,y_o,z_o)
    p_f = geo.Point3d(x_f,y_f,z_f)
    box = geo.BoundingBox(p_o,p_f).ToBrep()
    attr = giveColor(color)
    sc.doc.Objects.AddBrep(box,attr)
    sc.doc.Views.Redraw()
    return
 
"""
Render cuboid object in Rhino.

@param: [o]           object origin point (Point).
@param: [l]           object length (int/float).
@param: [w]           object width (int/float).
@param: [h]           object lheight (int/float).
@param: [orientation] orientation string (string).
@param: [color]       color string (string).
"""   
def renderCuboid(o,l,w,h,orientation='xyz',color='b'):
    s,on = [l,w,h],orientation
    x,y,z = 0.5*s[on.index('x')],0.5*s[on.index('y')],0.5*s[on.index('z')]
    x_o,y_o,z_o = o.x-x,o.y-y,o.z-z
    x_f,y_f,z_f = o.x+x,o.y+y,o.z+z
    p_o = geo.Point3d(x_o,y_o,z_o)
    p_f = geo.Point3d(x_f,y_f,z_f)
    box = geo.BoundingBox(p_o,p_f).ToBrep()
    attr = giveColor(color)
    sc.doc.Objects.AddBrep(box,attr)
    sc.doc.Views.Redraw()
    return

"""
Render tetrahedron object in Rhino.

@param: [o]           object origin point (Point).
@param: [r]           object rib length (int/float).
@param: [orientation] orientation string (string).
@param: [sense]       object top pointing sense string (string).
@param: [color]       color string (string).
"""     
def renderTetrahedron(o,r,orientation='xyz',sense='++',color='b'):
    c,i = [0.,0.,0.],1.
    if sense[0] == '-':
        i = -1.
    c['xyz'.index(orientation[2])] = i*sqrt(2./3.)*r
    x_1,y_1,z_1 = o.x+c[0],o.y+c[1],o.z+c[2]
    c,i = [0.,0.,0.],1.
    if sense[1] == '-':
        i = -1.
    c['xyz'.index(orientation[0])] = i*(sqrt(3.)/3.)*r
    x_2,y_2,z_2 = o.x+c[0],o.y+c[1],o.z+c[2]
    c['xyz'.index(orientation[0])] = -i*(sqrt(3.)/6.)*r
    c['xyz'.index(orientation[1])] = 0.5*r
    x_3,y_3,z_3 = o.x+c[0],o.y+c[1],o.z+c[2]
    c['xyz'.index(orientation[1])] = -0.5*r
    x_4,y_4,z_4 = o.x+c[0],o.y+c[1],o.z+c[2]
    mesh = geo.Mesh()
    mesh.Vertices.Add(x_1,y_1,z_1)
    mesh.Vertices.Add(x_2,y_2,z_2)
    mesh.Vertices.Add(x_3,y_3,z_3)
    mesh.Vertices.Add(x_4,y_4,z_4)
    mesh.Faces.AddFace(0,1,2)
    mesh.Faces.AddFace(0,1,3)
    mesh.Faces.AddFace(0,2,3)
    mesh.Faces.AddFace(1,2,3)
    attr = giveColor(color)
    sc.doc.Objects.AddMesh(mesh,attr)
    sc.doc.Views.Redraw()
    return

"""
Render octahedron object in Rhino.

@param: [o]           object origin point (Point).
@param: [r]           object rib length (int/float).
@param: [orientation] orientation string (string).
@param: [color]       color string (string).
""" 
def renderOctahedron(o,r,orientation='xyz',color='b'):
    c,h = [0.,0.,0.,],0.5*sqrt(2.)*r
    c['xyz'.index(orientation[2])] = h
    x_1,y_1,z_1 = o.x+c[0],o.y+c[1],o.z+c[2]
    c['xyz'.index(orientation[2])] = -h
    x_6,y_6,z_6 = o.x+c[0],o.y+c[1],o.z+c[2]
    c = [0.,0.,0.,]
    c['xyz'.index(orientation[0])] = 0.5*r
    c['xyz'.index(orientation[1])] = 0.5*r
    x_2,y_2,z_2 = o.x+c[0],o.y+c[1],o.z+c[2]
    c = [0.,0.,0.,]
    c['xyz'.index(orientation[0])] = -0.5*r
    c['xyz'.index(orientation[1])] = 0.5*r
    x_3,y_3,z_3 = o.x+c[0],o.y+c[1],o.z+c[2]
    c = [0.,0.,0.,]
    c['xyz'.index(orientation[0])] = 0.5*r
    c['xyz'.index(orientation[1])] = -0.5*r
    x_4,y_4,z_4 = o.x+c[0],o.y+c[1],o.z+c[2]
    c = [0.,0.,0.,]
    c['xyz'.index(orientation[0])] = -0.5*r
    c['xyz'.index(orientation[1])] = -0.5*r
    x_5,y_5,z_5 = o.x+c[0],o.y+c[1],o.z+c[2]
    mesh = geo.Mesh()
    mesh.Vertices.Add(x_1,y_1,z_1)
    mesh.Vertices.Add(x_2,y_2,z_2)
    mesh.Vertices.Add(x_3,y_3,z_3)
    mesh.Vertices.Add(x_4,y_4,z_4)
    mesh.Vertices.Add(x_5,y_5,z_5)
    mesh.Vertices.Add(x_6,y_6,z_6)
    mesh.Faces.AddFace(0,1,2)
    mesh.Faces.AddFace(0,1,3)
    mesh.Faces.AddFace(0,2,4)
    mesh.Faces.AddFace(0,3,4)
    mesh.Faces.AddFace(1,2,5)
    mesh.Faces.AddFace(1,3,5)
    mesh.Faces.AddFace(2,4,5)
    mesh.Faces.AddFace(3,4,5)
    attr = giveColor(color)
    sc.doc.Objects.AddMesh(mesh,attr)
    sc.doc.Views.Redraw()
    return

"""
Render truncated octahedron object in Rhino.

@param: [o]           object origin point (Point).
@param: [r]           object rib length (int/float).
@param: [r2]          object truncated rib length (int/float).
@param: [orientation] orientation string (string).
@param: [color]       color string (string).
"""     
def renderTruncOctahedron(o,r,r2,orientation='xyz',color='b'):
    c,h,w = [0.,0.,0.],0.25*sqrt(2.)*(r+r2),0.25*(r-r2)
    c['xyz'.index(orientation[2])] = h
    c['xyz'.index(orientation[0])] = w
    c['xyz'.index(orientation[1])] = w
    x1,y1,z1 = o.x+c[0],o.y+c[1],o.z+c[2]
    x24,y24,z24 = o.x-c[0],o.y-c[1],o.z-c[2]
    c['xyz'.index(orientation[0])] = -w
    x2,y2,z2 = o.x+c[0],o.y+c[1],o.z+c[2]
    x23,y23,z23 = o.x-c[0],o.y-c[1],o.z-c[2]
    c['xyz'.index(orientation[0])] = w
    c['xyz'.index(orientation[1])] = -w
    x3,y3,z3 = o.x+c[0],o.y+c[1],o.z+c[2]
    x22,y22,z22 = o.x-c[0],o.y-c[1],o.z-c[2]
    c['xyz'.index(orientation[0])] = -w
    x4,y4,z4 = o.x+c[0],o.y+c[1],o.z+c[2]
    x21,y21,z21 = o.x-c[0],o.y-c[1],o.z-c[2]
    c,h,w = [0.,0.,0.],0.25*sqrt(2.)*(r-r2),0.25*(r+r2)
    c['xyz'.index(orientation[2])] = h
    c['xyz'.index(orientation[0])] = w
    c['xyz'.index(orientation[1])] = w
    x5,y5,z5 = o.x+c[0],o.y+c[1],o.z+c[2]
    x20,y20,z20 = o.x-c[0],o.y-c[1],o.z-c[2]
    c['xyz'.index(orientation[0])] = -w
    x6,y6,z6 = o.x+c[0],o.y+c[1],o.z+c[2]
    x19,y19,z19 = o.x-c[0],o.y-c[1],o.z-c[2]
    c['xyz'.index(orientation[0])] = w
    c['xyz'.index(orientation[1])] = -w
    x7,y7,z7 = o.x+c[0],o.y+c[1],o.z+c[2]
    x18,y18,z18 = o.x-c[0],o.y-c[1],o.z-c[2]
    c['xyz'.index(orientation[0])] = -w
    x8,y8,z8 = o.x+c[0],o.y+c[1],o.z+c[2]
    x17,y17,z17 = o.x-c[0],o.y-c[1],o.z-c[2]
    c,k1,k2 = [0.,0.,0.],0.5*r,0.5*r2
    c['xyz'.index(orientation[0])] = k2
    c['xyz'.index(orientation[1])] = k1
    x9,y9,z9 = o.x+c[0],o.y+c[1],o.z+c[2]
    x13,y13,z13 = o.x-c[0],o.y-c[1],o.z-c[2]
    c['xyz'.index(orientation[0])] = k1
    c['xyz'.index(orientation[1])] = k2
    x10,y10,z10 = o.x+c[0],o.y+c[1],o.z+c[2]
    x14,y14,z14 = o.x-c[0],o.y-c[1],o.z-c[2]
    c['xyz'.index(orientation[1])] = -k2
    x11,y11,z11 = o.x+c[0],o.y+c[1],o.z+c[2]
    x15,y15,z15 = o.x-c[0],o.y-c[1],o.z-c[2]
    c['xyz'.index(orientation[0])] = k2
    c['xyz'.index(orientation[1])] = -k1
    x12,y12,z12 = o.x+c[0],o.y+c[1],o.z+c[2]
    x16,y16,z16 = o.x-c[0],o.y-c[1],o.z-c[2]
    mesh = geo.Mesh()
    mesh.Vertices.Add(x1,y1,z1)
    mesh.Vertices.Add(x2,y2,z2)
    mesh.Vertices.Add(x3,y3,z3)
    mesh.Vertices.Add(x4,y4,z4)
    mesh.Vertices.Add(x5,y5,z5)
    mesh.Vertices.Add(x6,y6,z6)
    mesh.Vertices.Add(x7,y7,z7)
    mesh.Vertices.Add(x8,y8,z8)
    mesh.Vertices.Add(x9,y9,z9)
    mesh.Vertices.Add(x10,y10,z10)
    mesh.Vertices.Add(x11,y11,z11)
    mesh.Vertices.Add(x12,y12,z12)
    mesh.Vertices.Add(x13,y13,z13)
    mesh.Vertices.Add(x14,y14,z14)
    mesh.Vertices.Add(x15,y15,z15)
    mesh.Vertices.Add(x16,y16,z16)
    mesh.Vertices.Add(x17,y17,z17)
    mesh.Vertices.Add(x18,y18,z18)
    mesh.Vertices.Add(x19,y19,z19)
    mesh.Vertices.Add(x20,y20,z20)
    mesh.Vertices.Add(x21,y21,z21)
    mesh.Vertices.Add(x22,y22,z22)
    mesh.Vertices.Add(x23,y23,z23)
    mesh.Vertices.Add(x24,y24,z24)
    mesh.Faces.AddFace(0,1,3,2)
    mesh.Faces.AddFace(20,21,23,22)
    mesh.Faces.AddFace(0,1,5,4)
    mesh.Faces.AddFace(0,2,6,4)
    mesh.Faces.AddFace(2,3,7,6)
    mesh.Faces.AddFace(1,3,7,5)
    mesh.Faces.AddFace(4,6,10,9)
    mesh.Faces.AddFace(6,11,12,7)
    mesh.Faces.AddFace(7,13,14,5)
    mesh.Faces.AddFace(5,15,8,4)
    mesh.Faces.AddFace(20,21,17,16)
    mesh.Faces.AddFace(20,22,18,16)
    mesh.Faces.AddFace(22,23,19,18)
    mesh.Faces.AddFace(21,23,19,17)
    mesh.Faces.AddFace(16,17,15,8)
    mesh.Faces.AddFace(16,9,10,18)
    mesh.Faces.AddFace(18,11,12,19)
    mesh.Faces.AddFace(19,13,14,17)
    mesh.Faces.AddFace(4,8,16,9)
    mesh.Faces.AddFace(5,14,17,15)
    mesh.Faces.AddFace(7,12,19,13)
    mesh.Faces.AddFace(6,10,18,11)
    attr = giveColor(color)
    mesh.UnifyNormals()
    if sc.doc.Objects.AddMesh(mesh,attr)!=sys.Guid.Empty:
        sc.doc.Views.Redraw()
    return
 
"""
Render capsule object in Rhino.

@param: [o]           object origin point (Point).
@param: [r]           object radius (int/float).
@param: [h]           object height (int/float).
@param: [orientation] orientation string (string).
@param: [color]       color string (string).
"""    
def renderCapsule(o,r,h,orientation='xyz',color='b'):
    c = [0.,0.,0.]
    c['xyz'.index(orientation[2])] = 0.5*h
    x_o,y_o,z_o = o.x-c[0],o.y-c[1],o.z-c[2]
    x_f,y_f,z_f = o.x+c[0],o.y+c[1],o.z+c[2]
    p_o,p_f = geo.Point3d(x_o,y_o,z_o),geo.Point3d(x_f,y_f,z_f)
    axis = p_f-p_o
    plane = geo.Plane(p_o,axis)
    circle = geo.Circle(plane,r)
    cyl = geo.Cylinder(circle,axis.Length).ToBrep(True, True)
    sphere1 = geo.Sphere(p_o,r)
    sphere2 = geo.Sphere(p_f,r)
    attr = giveColor(color)
    sc.doc.Objects.AddBrep(cyl,attr)
    sc.doc.Objects.AddSphere(sphere1,attr) 
    sc.doc.Objects.AddSphere(sphere2,attr) 
    sc.doc.Views.Redraw()
    return

"""
Render truncated capsule object in Rhino.

@param: [o]           object origin point (Point).
@param: [r]           object radius (int/float).
@param: [h]           object height (int/float).
@param: [r2]          object truncated radius (int/float).
@param: [h2]          object truncated height (int/float).
@param: [orientation] orientation string (string).
@param: [color]       color string (string).
"""     
def renderTruncCapsule(o,r,h,r2,h2,orientation='xyz',color='b'):
    c = [0.,0.,0.]
    c['xyz'.index(orientation[2])] = 0.5*h
    x_o,y_o,z_o = o.x-c[0],o.y-c[1],o.z-c[2]
    x_f,y_f,z_f = o.x+c[0],o.y+c[1],o.z+c[2]
    p_o,p_f = geo.Point3d(x_o,y_o,z_o),geo.Point3d(x_f,y_f,z_f)
    axis = p_f-p_o
    plane = geo.Plane(p_o,axis)
    circle = geo.Circle(plane,r)
    cyl = geo.Cylinder(circle,axis.Length).ToBrep(True, True)
    c2 = [0.,0.,0.]
    c2['xyz'.index(orientation[2])] = h2
    x_o,y_o,z_o = o.x-c[0]-c2[0],o.y-c[1]-c2[1],o.z-c[2]-c2[2]
    x_f,y_f,z_f = o.x+c[0]+c2[0],o.y+c[1]+c2[1],o.z+c[2]+c2[2]
    p_o_dot,p_f_dot = geo.Point3d(x_o,y_o,z_o),geo.Point3d(x_f,y_f,z_f)
    b1,t1 = geo.Circle(p_o,r),geo.Circle(p_o_dot,r2)
    b2,t2 = geo.Circle(p_f,r),geo.Circle(p_f_dot,r2)
    attr = giveColor(color)
    sc.doc.Objects.AddBrep(cyl,attr)
    curv1 = geo.LineCurve(b1.PointAt(0),t1.PointAt(0))
    axis1 = geo.Line(b1.Center,t1.Center)
    surf1 = geo.RevSurface.Create(curv1,axis1)
    cone1 = geo.Brep.CreateFromRevSurface(surf1, True, True)
    sc.doc.Objects.AddBrep(cone1,attr)
    curv2 = geo.LineCurve(b2.PointAt(0),t2.PointAt(0))
    axis2 = geo.Line(b2.Center,t2.Center)
    surf2 = geo.RevSurface.Create(curv2,axis2)
    cone2 = geo.Brep.CreateFromRevSurface(surf2, True, True)
    sc.doc.Objects.AddBrep(cone2,attr)
    sc.doc.Views.Redraw()
    return 


import BasicShapes as bs
h,w = 0.25*sqrt(2.)*(20.),0.25*(10.)
renderTruncOctahedron(bs.Point(0.,0.,0.),15.,5.,orientation='xyz',color='y')
renderTruncOctahedron(bs.Point(0.,0.,2*h),15.,5.,orientation='xyz',color='g')
renderTruncOctahedron(bs.Point(0.,4*w,h),15.,5.,orientation='xyz',color='pi')
renderTruncOctahedron(bs.Point(0.,-4*w,h),15.,5.,orientation='xyz',color='pi')
renderTruncOctahedron(bs.Point(-4*w,0.,-h),15.,5.,orientation='xyz',color='pi')
renderTruncOctahedron(bs.Point(4*w,0.,-h),15.,5.,orientation='xyz',color='pi')
renderTruncOctahedron(bs.Point(4*w,4*w,0.),15.,5.,orientation='xyz',color='p')
renderTruncOctahedron(bs.Point(-4*w,-4*w,0.),15.,5.,orientation='xyz',color='b')