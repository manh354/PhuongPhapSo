
import sys
sys.path.append('../PhuongPhapSo')

from Interpolation.TableAndPolynomial import *
from Interpolation.Langrange.Langrange import main as MainLangrange

def mainReverseLangrange(dataX, dataY):
    return MainLangrange(dataY, dataX)

