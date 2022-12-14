from InputProcess.InputInterface import main as InputMain
from ValuesConvert import*
from FindX0Mode import*

from Langrange.Langrange import main as LangrangeMain
from Newton.NewtonForward import mainAny as NewtonForwardAnyMain
from Newton.NewtonForward import mainEqui as NewtonForwardEquiMain
from Newton.NewtonBackward import mainAny as NewtonBackwardAnyMain
from Newton.NewtonBackward import mainEqui as NewtonBackwardEquiMain
from Center.Bessel import mainBesselNorm as BesselNormMain
from Center.Bessel import mainBesselSkewed as BesselSkewedMain
from Center.Stirling import main as StirlingMain
from Center.Gauss import mainGauss1 as Gauss1Main
from Center.Gauss import mainGauss2 as Gauss2Main
from ReverseInterpolation.ReverseLangrange import mainReverseLangrange as ReverseLangrangeMain
from ReverseInterpolation.ReverseNewton import mainNewtonForward as ReverseNewtonForwardMain
from ReverseInterpolation.ReverseNewton import mainNewtonBackward as ReverseNewtonBackwardMain

from TableAndPolynomial import CalcPolyReversedInput

from enum import Enum

def menuNoisuy():
    print("Chon PHUONG PHAP ban muon su dung")
    print("1: Langrange")
    print("2: Newton")
    print("3: Gauss")
    print("4: Bessel")
    print("5: Stirling")
    mode = input()
    if(mode == "1"):
        return LangrangeMain, NotConvert, NoMark
    elif(mode == "2"):
        return menuNewton()
    elif(mode == "3"):
        return menuGauss()
    elif(mode == "4"):
        return menuBessel()
    return StirlingMain, ConvertXtoT, MarkAtCenter


def menuGauss():
    print("Chon loai phuong phap gauss ban muon su dung:")
    print("1: Gauss 1 (chon ben phai truoc ben trai sau)")
    print("2: Gauss 2 (chon ben trai truoc ben phai sau)")
    mode = input()
    if(mode == "1"):
        return Gauss1Main, ConvertXtoT, MarkAtCenter
    return Gauss2Main, ConvertXtoT, MarkAtCenter

def menuBessel():
    print("Chon loai phuong phap Bessel ban muon su dung:")
    print("1: Bessel theo t")
    print("2: Bessel theo u")
    mode = input()
    if(mode == "1"):
        return BesselNormMain, ConvertXtoT, MarkAtCenter
    return BesselSkewedMain, ConvertXtoU, MarkAtCenter

def menuNewton():
    print("Chon loai phuong phap newton ban muon su dung:")
    print("1: Newton TIEN voi moc bat ki")
    print("2: Newton TIEN voi moc CACH DEU")
    print("3: Newton lui voi moc bat ki")
    print("4: Newton lui voi moc CACH DEU")
    mode = input()
    if(mode == "1"):
        return NewtonForwardAnyMain, NotConvert, NoMark
    elif(mode == "2"):
        return NewtonForwardEquiMain, ConvertXtoT, MarkAtStart
    elif(mode == "3"):
        return NewtonBackwardAnyMain, NotConvert, NoMark
    return NewtonBackwardEquiMain, ConvertXtoT, MarkAtEnd

def menuNoisuyNguoc():
    print("Chon PHUONG PHAP ban muon su dung")
    print("1: Langrange Nguoc")
    print("2: Lap newton xuoi")
    print("3: Lap newton nguoc")
    mode = input()
    if(mode == "1"):
        return ReverseLangrangeMain
    elif (mode == "2"):
        return ReverseNewtonForwardMain
    return ReverseNewtonBackwardMain

#################################################################################
listOfPointsPath = "inputData.csv"
interpolatePoint = "inputPoint.csv"
### kiểm tra đầu vào
dataX, dataY, CoBiTrungLapKhong = InputMain(listOfPointsPath,'x','y')
if(CoBiTrungLapKhong):
    print("Du lieu bi TRUNG LAP... chua xu ly dc")
    exit()
print("Du lieu hop ly, Tiep tuc xu ly")

print("Ban muon chon du lieu trong khoang nao?")

print("Chon BAI TOAN ban muon giai")
print("1: Noi Suy")
print("2: Noi Suy Nguoc")
print("3: Tinh dao ham")
print("4: Tinh tich phan\n")

char1 = input()
if char1 == "1":
    print("Chon diem ban muon tinh noi suy:")
    value = input()
    noiSuy, conversion, mark = menuNoisuy()
    polyTable,poly = noiSuy(dataX, dataY)
    CalcPolyReversedInput(poly,value)

elif char1 == "2":
    noiSuyNguoc = menuNoisuyNguoc()
