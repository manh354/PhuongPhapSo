import sys
sys.path.append('../PhuongPhapSo')

from TableAndPolynomial import *

# cách chọn chỉ số của gauss1 trên bảng sai phân
#===============================
#
#
#
#   -  
#       -   -
#               -   -
#                       -   -
#===============================

def mainGauss1(dataX, dataY):
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    diffTable = CreateDifferenceTable(dataX,dataY)
    facTable = CreateFactorialTable(length)
    middle = int(len(dataX)/2) #khai bao vi tri giua
    print(diffTable)
    for i in range(1,length):
        offset:int #khai bao so chi p(p-1)(p+1)..(p+ offset)
        if i%2==0:
            offset = int(i/2)
        else:
            offset = int(-i/2)
        polyTable.append(MulTwoPoly(polyTable[i-1], CreateRootPoly(offset)))
    for i in range(0, length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[middle+ int((i+1)/2),i]/ facTable[i])
    poly = ConvertPolyTableToPoly(polyTable)
    return polyTable, poly

# cách chọn chỉ số của gauss2 trên bảng sai phân
#===============================
#
#
#
#   -   -
#           -   -
#                   -   -
#                           -
#===============================
def mainGauss2(dataX, dataY):
    length = len(dataX)
    polyTable = []
    polyTable.append([1])
    diffTable = CreateDifferenceTable(dataX,dataY)
    facTable = CreateFactorialTable(length)
    middle = int(len(dataX)/2) #khai bao vi tri giua
    print(diffTable)
    for i in range(1,length):
        offset:int #khai bao so chi p(p-1)(p+1)..(p + offset)
        if i%2!=0:
            offset = int(i/2)
        else:
            offset = int(-i/2)
        polyTable.append(MulTwoPoly(polyTable[i-1], CreateRootPoly(offset)))
    for i in range(0, length):
        polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[middle+ int(i/2),i]/ facTable[i])
    poly = ConvertPolyTableToPoly(polyTable)
    return polyTable, poly


polyTable,poly = mainGauss2([1,2,3,4,5,6,7],[1.1,1.2,1.4,1.8,2.6,4.2,7.4])
print("===================")
print(poly)
print("===================")
value = CalcPolyReversedInput(poly,0.5)
print(value)
p = list(poly)
p.reverse()
print(p)