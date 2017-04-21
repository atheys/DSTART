import Rhino
import scriptcontext
import System
import rhinoscriptsyntax as rs



def AddBrepBox():
    pt0 = Rhino.Geometry.Point3d(0, 0, 0)
    pt1 = Rhino.Geometry.Point3d(10, 10, 10)
    box = Rhino.Geometry.BoundingBox(pt0, pt1)
    brep = box.ToBrep()
    rc = Rhino.Commands.Result.Failure
    if( scriptcontext.doc.Objects.AddBrep(brep) != System.Guid.Empty ):
        rc = Rhino.Commands.Result.Success
        scriptcontext.doc.Views.Redraw()
    return rc
    
def AddMaterial():
    # materials are stored in the document's material table
    index = scriptcontext.doc.Materials.Add()
    mat = scriptcontext.doc.Materials[index]
    mat.DiffuseColor = System.Drawing.Color.Blue
    mat.SpecularColor = System.Drawing.Color.CadetBlue
    mat.CommitChanges()

    # set up object attributes to say they use a specific material
    sp = Rhino.Geometry.Sphere([0,0,0], 5)
    attr = Rhino.DocObjects.ObjectAttributes()
    attr.MaterialIndex = index
    attr.MaterialSource = Rhino.DocObjects.ObjectMaterialSource.MaterialFromObject
    scriptcontext.doc.Objects.AddSphere(sp, attr)

    scriptcontext.doc.Views.Redraw()
    return

def AddMesh():
    index = scriptcontext.doc.Materials.Add()
    mat = scriptcontext.doc.Materials[index]
    mat.DiffuseColor = System.Drawing.Color.Blue
    mat.SpecularColor = System.Drawing.Color.CadetBlue
    mat.CommitChanges()
    attr = Rhino.DocObjects.ObjectAttributes()
    attr.MaterialIndex = index
    attr.MaterialSource = Rhino.DocObjects.ObjectMaterialSource.MaterialFromObject
    
    mesh = Rhino.Geometry.Mesh()
    mesh.Vertices.Add(0.0, 0.0, 0.0) #0
    mesh.Vertices.Add(10.0, 10.0, 0.0) #1
    mesh.Vertices.Add(2.0, -15.0, 0.0) #2
    mesh.Vertices.Add(3.0, 5.0, 10.0) #3
    mesh.Faces.AddFace(0,1,2)
    mesh.Faces.AddFace(0,1,3)
    mesh.Faces.AddFace(0,2,3)
    mesh.Faces.AddFace(1,2,3)
    if scriptcontext.doc.Objects.AddMesh(mesh,attr)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

def AddTruncatedCone():
    bottom_pt = Rhino.Geometry.Point3d(0,0,0)
    bottom_radius = 2
    bottom_circle = Rhino.Geometry.Circle(bottom_pt, bottom_radius)

    top_pt = Rhino.Geometry.Point3d(0,0,10)
    top_radius = 6
    top_circle = Rhino.Geometry.Circle(top_pt, top_radius)

    shapeCurve = Rhino.Geometry.LineCurve(bottom_circle.PointAt(0), top_circle.PointAt(0))
    axis = Rhino.Geometry.Line(bottom_circle.Center, top_circle.Center)
    revsrf = Rhino.Geometry.RevSurface.Create(shapeCurve, axis)
    tcone_brep = Rhino.Geometry.Brep.CreateFromRevSurface(revsrf, True, True)

    if scriptcontext.doc.Objects.AddBrep(tcone_brep)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure
if( __name__ == "__main__" ):
    bottom_pt = Rhino.Geometry.Point3d(0,0,0)
    bottom_radius = 2
    bottom_circle = Rhino.Geometry.Circle(bottom_pt, bottom_radius)

    top_pt = Rhino.Geometry.Point3d(0,0,10)
    top_radius = 6
    top_circle = Rhino.Geometry.Circle(top_pt, top_radius)

    shapeCurve = Rhino.Geometry.LineCurve(bottom_circle.PointAt(0), top_circle.PointAt(0))
    axis = Rhino.Geometry.Line(bottom_circle.Center, top_circle.Center)
    revsrf = Rhino.Geometry.RevSurface.Create(shapeCurve, axis)
    tcone_brep = Rhino.Geometry.Brep.CreateFromRevSurface(revsrf, True, True)

    if scriptcontext.doc.Objects.AddBrep(tcone_brep)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()

