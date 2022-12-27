import sys
sys.path.append('../PhuongPhapSo')

from Interpolation.TableAndPolynomial import *
from Interpolation.ValuesConvert import *

def mainAny(dataX, dataY):
    """
    Newton tiến với mốc bất kì (giữ nguyên biến x)
    """
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    #print(polyTable[0])
    divTable = CreateDividedTable(dataX, dataY)
    print(divTable)
    for i in range(1,length):
        polyTable.append(MulTwoPoly(polyTable[i-1],CreateRootPoly(dataX[i-1])))
    for i in range(0,length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], divTable[i,i])
    poly = ConvertPolyTableToPoly(polyTable)
    return polyTable, poly



def mainEqui(dataX, dataY):
    """
    Newton tiến với mốc cách đều (đổi biến sang t)
    """
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    #print(polyTable[0])
    diffTable = CreateDifferenceTable(dataX, dataY)
    facTable = CreateFactorialTable(length)
    print(diffTable)
    for i in range(1,length):
        polyTable.append(MulTwoPoly(polyTable[i-1],CreateRootPoly(i-1)))
    for i in range(0,length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[i,i] / facTable[i])
    poly = ConvertPolyTableToPoly(polyTable)
    return polyTable, poly
