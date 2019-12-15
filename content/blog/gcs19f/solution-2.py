import numpy as np

class Surface():
    def __init__(self, faces):
      self.faces = faces
      vertices = set(i for f in faces for i in f)
      self.V = max(vertices)+1

    def is_surface(self):
      raise NotImplementedError
      
    def is_connected(self):
      raise NotImplementedError
    
    def is_oriented(self):
      raise NotImplementedError

    def is_orientable(self):
      raise NotImplementedError
                
    def Euler(self):
      raise NotImplementedError

