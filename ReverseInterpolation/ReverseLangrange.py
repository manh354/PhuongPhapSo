
import sys
sys.path.append('../PhuongPhapSo')

from TableAndPolynomial import *
from Langrange.Langrange import main as MainLangrange

def mainReverseLangrange(dataX, dataY):
    return MainLangrange(dataY, dataX)

