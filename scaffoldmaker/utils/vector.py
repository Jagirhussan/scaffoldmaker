'''
Utility functions for vectors.
Created on Apr 13, 2018

@author: Richard Christie
'''

import math

def crossproduct3(a, b):
    '''
    :return: vector 3-D cross product of a and b
    '''
    return [ a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0] ]

def dotproduct(a, b):
    '''
    :return: vector dot (inner) product of a and b
    '''
    return sum(a[i]*b[i] for i in range(len(a)))

def magnitude(v):
    '''
    return: scalar magnitude of vector v
    '''
    return math.sqrt(sum(c*c for c in v))

def normalise(v):
    '''
    :return: vector v normalised to unit length
    '''
    mag = math.sqrt(sum(c*c for c in v))
    return [ c/mag for c in v ]
