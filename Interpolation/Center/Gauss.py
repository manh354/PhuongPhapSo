import sys
sys.path.append('../PhuongPhapSo')

from Interpolation.tableAndPolynomial import *

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
    middle = int((len(dataX)-1)/2) #khai bao vi tri giua
    print("Bảng sai phân:")
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
    middle = int(len(dataX)/2) #khai bao vi tri giua tuc la x0
    print("Bảng sai phân:")
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

