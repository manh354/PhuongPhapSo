import sys
sys.path.append('../PhuongPhapSo')

from TableAndPolynomial import *
from ValuesConvert import *

def mainAny(dataX: list, dataY: list):
    """
    Newton lùi với mốc bất kì (giữ nguyên biến x)
    """
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    #print(polyTable[0])
    divTable = CreateDividedTable(dataX, dataY)
    print(divTable)
    for i in range(1,length):
        polyTable.append(MulTwoPoly(polyTable[i-1],CreateRootPoly(dataX[-i])))
    for i in range(0,length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], divTable[-1,i])
    poly = ConvertPolyTableToPoly(polyTable)
    return polyTable, poly



def mainEqui(dataX: list, dataY: list):
    """
    Newton lùi với mốc cách đều (đổi biến sang t)
    """
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    #print(polyTable[0])
    diffTable = CreateDifferenceTable(dataX, dataY)
    facTable = CreateFactorialTable(length)
    print(diffTable)
    for i in range(1,length):
        polyTable.append(MulTwoPoly(polyTable[i-1],CreateRootPoly(-i+1)))
    for i in range(0,length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[-1,i] / facTable[i])
    poly = ConvertPolyTableToPoly(polyTable)
    return polyTable, poly


x = 1.5

polyTable,poly = mainAny([1,2,3,4,5,6],[1.1,1.2,1.4,1.8,2.6,4.2])
print("===================")
print(poly)
print("===================")
value = CalcPolyReversedInput(poly,5.5)
print(value)
p = list(poly)
p.reverse()
print(p)