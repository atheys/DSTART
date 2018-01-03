
from math import sqrt,log10,cos,sin,pi
import numpy as np

c = 3.*10**8
k = pi/3.
n1,n2 = (0.,0.,1.),(cos(k),0.,sin(k))
n3,n4 = (0.,cos(k),sin(k)),(-cos(k),0.,sin(k))
n5,n6 = (0.,-cos(k),sin(k)),(1./sqrt(2),-1./sqrt(2),0.)
n7,n8 = (1./sqrt(2),1./sqrt(2),0.),(-1./sqrt(2),1./sqrt(2),0.)
n9,n10 = (-1./sqrt(2),-1./sqrt(2),0.),(cos(k),0.,-sin(k))
n11,n12 = (0.,cos(k),-sin(k)),(-cos(k),0.,-sin(k))
n13,n14 = (0.,-cos(k),-sin(k)),(0.,0.,-1.)
normals = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14]

def standardize(angle):
    angle = float(angle)
    # Edge case: already standardized  
    if 0. <= angle and angle < 2.*pi :
        return angle
    else:
        while angle > 2.*pi :
            angle -= 2.*pi
        while angle < 0. :
            angle += 2.*pi
        return angle

def dotProduct(v,n):
    return sum(np.array(v)*np.array(n))

def indicator(x):
    x = float(x)
    if x < 0. : 
        return 0.
    else:
        return x

def computeAngularFactor(theta,phi,plane):
    # Edge Case
    if theta == None or phi == None:
        return 1.
    theta,phi,plane = standardize(theta),standardize(phi),int(plane)
    x,y,z = cos(phi)*cos(theta),cos(phi)*sin(theta),sin(phi)
    direct = np.array([x,y,z])
    dot = dotProduct(direct,normals[plane-1])
    if dot > 0.:
        return dot
    else:
        return 0.
    
class RadComp(object):
    
    def __init__(self,f,E,theta = None,phi = None):
        self.f = float(f)
        self.E = float(E)
        self.theta = theta
        self.phi = phi
        if theta is None and phi is None:
            self.directed = False
            self.factors = 14*[1.]
        else:
            self.directed = True
            self.theta = float(theta)
            self.phi = float(phi)
            self.factors = []
            for i in range(1,15):
                self.factors.append(computeAngularFactor(theta,phi,i))
    
    def rate(self,A,frac=0.1):
        A,frac = float(A),float(frac)
        return self.E*A*frac*c
    
    def absorption(self,t,material):
        t,g,mu = float(t),float(material.g),float(material.mu)
        A = log10(131.4*t*sqrt(self.f*mu*g))
        return A
      
    def reflection(self,t,material):
        t,g,mu = float(t),float(material.g),float(material.mu)
        R = 168.-20.*log10(sqrt(self.f*mu/g))
        return R
        
    def re_reflection(self,t,material):
        t,f,g,mu = float(t),self.f,float(material.g),float(material.mu)
        A,R = self.absorption(t,material),0.
        if A<10.:
            m = (9.77*10.**10)*sqrt(f*mu/g)
            nom1 = 4.*((1.-m**2)**2-2.*m**2)
            nom2 = 4.*(2.*sqrt(2)*m*(1.-m)**2)
            denom = ((1.+sqrt(2)*m)**2+1.)**2
            c1 = complex(nom1/denom,nom2/denom)
            c2 = complex(cos(0.23*A),-sin(0.23*A))
            R = 20.*log10((1.-c1*c2).real)
            if R > 0.:
                return R
            else:
                return 0.
        return R
    
    def shielding(self,t,material):
        A,R,C = self.absorption(t,material),self.reflection(t,material),self.re_reflection(t,material)
        return A+R-C
 

class Radiation(object):
    
    def __init__(self,radcomps):
        self.rads = list(radcomps)
    
    def addRadiation(self,rad):
        self.rads.append(rad)
    
    def shielding(self,plane,A,t,material,exp=1.,frac=0.1):
        exp,plane,sh = float(exp),int(plane),[]
        for rad in self.rads:
            sh.append((rad.shielding(t,material)/10.)**exp)
        return sh
        
    def energyRate(self,plane,A,crossed,frac=0.1):
        plane,A = int(plane),float(A)
        exp,total = np.array(len(self.rads)*[0.]),0.
        for wall in crossed:
            exp = exp + np.array(self.shielding(plane,A,wall[0],wall[1]))
        for r in range(len(self.rads)):
            rad = self.rads[r]
            total += 1.*rad.E*A*c*computeAngularFactor(rad.theta,rad.phi,plane)*10.**(-exp[r])
        return total

def area(plane,r):
    plane = int(plane)
    if plane in [1,6,7,8,9,14]:
        return r**2
    else:
        return 1.5*sqrt(3)*r**2

def radiationLevels(node,radiation,ugrid):
    import GridCreator as GC
    i,j,k = int(node[0]),int(node[1]),int(node[2])
    module = ugrid[i][j][k]
    level = 0.
    for i in range(1,15):
        A,loop,crossed = area(i,module.r),True,[(module.t,module.material)]
        while loop:
            actual,numbers = GC.neighbors(node,ugrid,True)
            if i not in numbers:
                n = actual[numbers.index(i)]
                x,y,z = int(n[0]),int(n[1]),int(n[2])
                nmodule = ugrid[x][y][z]
                crossed.append((nmodule.t,nmodule.material))
                crossed.append((nmodule.t,nmodule.material))
            else: 
                loop = False
        level += radiation.energyRate(i,A,crossed)
    return level