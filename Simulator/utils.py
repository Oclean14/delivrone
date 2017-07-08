from math import pow, sqrt

def dist(pA, pB):
    return sqrt(pow(pB[0] - pA[0], 2) + pow(pB[1] - pA[1], 2))

def vec2d_multiply():
    return

def vec2d_add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def vec2d_sub(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def vec2d_multiply_scalar(v, scalar):
    return (v[0] * scalar, v[1] * scalar)

def vec2d_magnitude(v):
    return sqrt(pow(v[0], 2) + pow(v[1], 2))

def vec2d_normalize(v):
    return (v[0] / vec2d_magnitude(v), v[1] / vec2d_magnitude(v))
