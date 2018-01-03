"""
Modules Module.
@author: Andreas Theys.
@version: 2.0
"""

from ComplexShapes import TruncOctahedron as Toc

def colorIndication(label):
    label = str(label)
    if label == 'Habitation':
        return 'y'
    elif label == 'Life Support':
        return 'g'
    elif label == 'Mining':
        return 'r' 
    elif label == 'Processing':
        return 'o'
    elif label == 'Manufacturing':
        return 'b'
    elif label == 'Ore Storage':    
        return 'i'
    elif label == 'Refined Storage': 
        return 'p'
    elif label == 'Radiation Shielding': 
        return 'pi'
    elif label == 'Collision Shielding': 
        return 'gr'
    elif label == 'Thrust': 
        return 'w'
    else:
        return 'k'
        
class Module(object):
    
    def __init__(self,label,center,R,t,material):
        self.label = str(label)
        self.c = center
        self.R = float(R)
        self.r = float(R)/3.
        self.color = colorIndication(self.label)
        self.mod = Toc(self.c,self.R)
        self.t = float(t)
        self.material = material