import numpy as np
import math

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def right_turn(vector):
    return np.array([-vector[1],vector[0]])

def circumcenter(triangle):
    '''
    given a triangle as a numpy matrix of shape (3,2), returns its circumcenter
    '''
    D = 2*np.sum(np.cross(triangle[:,0],triangle[:,1]))
    norms = np.array([np.dot(triangle[i],triangle[i]) for i in range(3)])
    U = [np.sum(np.cross(triangle[:,i], norms)) for i in range(2)]
    if D==0:
        return None
    return right_turn(U)/D

class curve_transform:
    def __init__(self, curve=None):
        self.number_of_steps = 10**3
        self.step = .1/self.number_of_steps
        if curve == None:
            curve = [(0,0),(0,1),(1,1),(1,0)]
        self.curve = np.array(curve)
        self.n = len(self.curve)
        self.curvature_definitions = ['A', 'B', 'C', 'D'] 
        # A,B,C are corresponding definitions from Steiner's formula, and D is by osculating circle
        self.curvature_definition = 'A'

    def previous_edge(self, vertex):
        '''
        returns the vector from the previous vertex to the given one
        '''
        raise NotImplementedError

    def next_edge(self, vertex):
        '''
        returns the vector from the given vertex to the next one
        '''
        raise NotImplementedError


    def turning_angle(self, vertex): 
        '''
        returns the turning angle (angle between directions of previous and next edges) at given vertex
        '''
        raise NotImplementedError

    def curvature(self, vertex):
        '''
        returns the curvature k at given vertex
        '''
        raise NotImplementedError

    def N(self, vertex):
        '''
        returns the normal vector at given vertex
        '''
        raise NotImplementedError

    def kN(self, vertex):
        '''
        returns k*N at given vertex
        '''
        raise NotImplementedError

    def flow(self):
        '''
        returns an np.array of vectors kN at all vertices
        '''
        raise NotImplementedError

    def transform(self):
        '''
        replaces curve with curve+step*flow number_of_steps times (forward Euler method)
        '''
        raise NotImplementedError

    def is_round(self):
        '''
        checks whether vertices lie on a circle and returns a boolean value
        '''
        raise NotImplementedError

    def mass_center(self):
        '''
        returns the center of mass of the curve
        '''
        raise NotImplementedError

    def total_curvature(self):
        '''
        returns the total curvature of the curve
        '''
        raise NotImplementedError
