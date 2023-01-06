# da thuc Langrange co cong thuc la : Tong sigma (0,n) yi/Di  * (w_n+1(x))/(x-xi)

from Interpolation.Langrange.dataSlicingLangrange import sliceInputFromLeftToRight
from Interpolation.Langrange.dataOutputLangrange import output
import sys
sys.path.append('../PhuongPhapSo')

import numpy as np
from Interpolation.tableAndPolynomial import *

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

def mainLangrange(dataX, dataY):
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
    return w, polynomials, poly

def wrapperLangrange(dataX, dataY, x):
    dataX, dataY = sliceInputFromLeftToRight(dataX,dataY)
    w, all_polynomials, final_polynomial = mainLangrange(dataX,dataY)
    interpolate_polynomial_value_at_x = CalcPolyReversedInput(final_polynomial,x)
    output(dataX, dataY,w,all_polynomials,final_polynomial, x, interpolate_polynomial_value_at_x)
    return final_polynomial
