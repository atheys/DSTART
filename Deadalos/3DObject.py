"""
3DObject Module.

@author: Andreas Theys.
@version: 1.0
"""

"""
Color Object Class.
"""
class Color(object):
    
    """
    Basic Constructor.
    
    @param: [color] color.
    """
    def __init__(self,color):
        self.c = str(color)
        return


"""
3DObject Object Class.
"""
class Object(object):
    
    """
    Basic Constructor.
    
    @param: [obj]         object to render.
    @param: [orientation] orientation of the object (string).
    """
    def __init__(self,obj,orientation=''):
        self.obj = obj
        self.orien = orientation
        return
        