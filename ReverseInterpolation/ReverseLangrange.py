
import sys
sys.path.append('../PhuongPhapSo')

from TableAndPolynomial import *
from Langrange.Langrange import main as MainLangrange

def mainReverseLangrange(dataX, dataY):
    return MainLangrange(dataY, dataX)

table, poly = mainReverseLangrange([1,2,3,4,5,6],[1.1,1.2,1.4,1.8,2.6,4.2])
testValue = CalcPolyReversedInput(poly,1.5)
print(testValue)