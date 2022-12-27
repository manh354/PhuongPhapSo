# da thuc Langrange co cong thuc la : Tong sigma (0,n) yi/Di  * (w_n+1(x))/(x-xi)

import sys
sys.path.append('../PhuongPhapSo')

import numpy as np

from Interpolation.TableAndPolynomial import *

def CalculateDiValue(roots: list, position):
    result = 1
    for i in range(0,len(roots)):
        if(i != position):
            result *= roots[position] - roots[i]
    return result

def CalcWPolynomial(roots: list):
    poly = CreateRootPoly(roots[0])
    for i in range(1, len(roots)):
        poly = MulTwoPoly(poly,CreateRootPoly(roots[i]))
    return poly

def ConvertLangrangeTableToPoly(table: list):
    poly = np.zeros(len(table))
    for j in range(0, len(table)):
        for i in range(0, len(table)):
            poly[j] += table[i][j]
    return poly

def main(dataX, dataY):
    polynomials = []
    length = len(dataX)
    w = CalcWPolynomial(dataX)
    for i in range(0,length):
        Di = CalculateDiValue(dataX,i)
        ithPolynomial = HornerDivideReversedInput(w,dataX[i])
        #print(ithPolynomial)
        ithPolynomial = MulPolyWithCoef(ithPolynomial, dataY[i]/Di)
        polynomials.append(ithPolynomial)
    poly = ConvertLangrangeTableToPoly(polynomials)
    return polynomials, poly

x = []
for i in range(-4,5):
    x.append(i/4)
_, p = main([-1.1152742105263158, -1.2073642105263158, -1.2494842105263158, -1.2481342105263158, -1.2082042105263158, -1.1332242105263157, -1.0255742105263157, -0.5172542105263158, -0.28588421052631574],x)
print(p)
v = CalcPolyReversedInput(p,-1.25)
print(v)