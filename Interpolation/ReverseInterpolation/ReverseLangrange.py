
import sys
sys.path.append('../PhuongPhapSo')

from Interpolation.tableAndPolynomial import *
from Interpolation.Langrange.langrange import mainLangrange as MainLangrange

def mainReverseLangrange(dataX, dataY):
    return MainLangrange(dataY, dataX)

