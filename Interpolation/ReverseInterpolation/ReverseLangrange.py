
import sys
sys.path.append('../PhuongPhapSo')

from Interpolation.tableAndPolynomial import *
from Interpolation.Langrange.langrange import wrapperLangrange as MainLangrange

def mainReverseLangrange(dataX, dataY,y):
    return MainLangrange(dataY, dataX,y)

