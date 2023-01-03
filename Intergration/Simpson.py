from FindStep import main as FindStep
import sympy as sp
import numpy as np
import math

func = "E^(sin(x)+cos(x))"
var = sp.Symbol('x')
segment_a = 0
segment_b = 1
eps0 = 5e-8

h = FindStep(func, var, eps0, segment_a, segment_b, 0.1, 10e-3,100)
numSteps = int(math.ceil((segment_b - segment_a)/h)+1)
list_y = np.linspace(segment_a,segment_b,numSteps)
list_y[0] = list_y[0] / 2
list_y[len(list_y)-1] = list_y[len(list_y)-1] /2
list_y = np.multiply(list_y,h)
sum_y = np.sum(list_y) 

print(sum_y)