from Interpolation.InputProcess.InputInterface import main as InputMain
from Interpolation.InputProcess.SliceData import SliceFromTo, AutoSlice, AutoFindSlice, SliceByHand
from Interpolation.ValuesConvert import*
from FindX0Mode import*

from Interpolation.Langrange.Langrange import main as LangrangeMain
from Interpolation.Newton.NewtonForward import mainAny as NewtonForwardAnyMain
from Interpolation.Newton.NewtonForward import mainEqui as NewtonForwardEquiMain
from Interpolation.Newton.NewtonBackward import mainAny as NewtonBackwardAnyMain
from Interpolation.Newton.NewtonBackward import mainEqui as NewtonBackwardEquiMain
from Interpolation.Center.Bessel import mainNorm as BesselNormMain
from Interpolation.Center.Bessel import mainSkewed as BesselSkewedMain
from Interpolation.Center.Stirling import main as StirlingMain
from Interpolation.Center.Gauss import mainGauss1 as Gauss1Main
from Interpolation.Center.Gauss import mainGauss2 as Gauss2Main
from Interpolation.ReverseInterpolation.ReverseLangrange import mainReverseLangrange as ReverseLangrangeMain
from Interpolation.ReverseInterpolation.ReverseNewton import mainNewtonForward as ReverseNewtonForwardMain
from Interpolation.ReverseInterpolation.ReverseNewton import mainNewtonBackward as ReverseNewtonBackwardMain

from Interpolation.TableAndPolynomial import CalcPolyReversedInput


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
    return StirlingMain, ConvertXtoT, MarkAtCenterLeft


def menuGauss():
    print("Chon loai phuong phap gauss ban muon su dung:")
    print("1: Gauss 1 (chon ben phai truoc ben trai sau)")
    print("2: Gauss 2 (chon ben trai truoc ben phai sau)")
    mode = input()
    if(mode == "1"):
        return Gauss1Main, ConvertXtoT, MarkAtCenterLeft
    return Gauss2Main, ConvertXtoT, MarkAtCenterRight

def menuBessel():
    print("Chon loai phuong phap Bessel ban muon su dung:")
    print("1: Bessel theo t")
    print("2: Bessel theo u")
    mode = input()
    if(mode == "1"):
        return BesselNormMain, ConvertXtoT, MarkAtCenterLeft
    return BesselSkewedMain, ConvertXtoU, MarkAtCenterLeft

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
def main():
    listOfPointsPath = "inputData.csv"
    interpolatePoint = "inputPoint.csv"
    sliceMode = "tay"
    ### kiểm tra đầu vào
    dataX, dataY, CoBiTrungLapKhong, CoCachDeuNhauKhong = InputMain(listOfPointsPath,'x','y')
    if(CoBiTrungLapKhong):
        print("Du lieu bi TRUNG LAP... chua xu ly dc")
        exit()
    print("Du lieu hop ly, Tiep tuc xu ly")
    h = dataX[1] - dataX[0]
    if(CoCachDeuNhauKhong):
        print("Du lieu CACH DEU nhau")
    else:
        print("Du lieu KHONG cach deu nhau")

    print("Ban muon chon du lieu trong khoang nao?")

    print("Chon BAI TOAN ban muon giai")
    print("1: Noi Suy")
    print("2: Noi Suy Nguoc")
    print("3: Tinh dao ham")
    print("4: Tinh tich phan\n")

    char1 = input()
    if char1 == "1":
        noiSuy, conversion, mark = menuNoisuy()
        ## Chọn điểm tính mốc
        print("Chon diem ban muon tinh noi suy:")
        value = float(input())
        ## Chọn số mốc nội suy
        print("Chọn mốc nội suy ngoài cùng bên trái:")
        left = float(input())
        print("Chọn mốc nội suy ngoài cùng bên phải:")
        right = float(input())
        ## Xử lý mốc nội suy
        ndataX, ndataY = SliceByHand(dataX,dataY,left, right)
        ## Xử lý nội suy
        polyTable,poly = noiSuy(ndataX, ndataY)
        print("Điểm neo t là {0}".format(mark(ndataX)))
        ketquaNoiSuy = CalcPolyReversedInput(poly,conversion(value, mark(ndataX), h))
        print("Kết quả tính toán nội suy tại x = {0}, tương đương t = {1} là: {2}".format(value,conversion(value, mark(ndataX), h), ketquaNoiSuy))
    elif char1 == "2":
        noiSuyNguoc = menuNoisuyNguoc()
        if noiSuyNguoc == ReverseLangrangeMain:
            print("Nhập điểm bạn muốn tính nội suy ngược:")
            value = float(input())
            print("Chọn mốc nội suy ngoài cùng bên trái:")
            left = int(input())
            print("Chọn mốc nội suy ngoài cùng bên phải:")
            right = int(input())
            ndataX, ndataY = SliceByHand(dataX,dataY,left, right)
            polyTable,poly = noiSuyNguoc(ndataX, ndataY)
            ketquaNoiSuy = CalcPolyReversedInput(poly, value)
            print("Kết quả tính toán nội suy ngược tại y = {0} là: {1}".format(value,ketquaNoiSuy))
        if noiSuyNguoc == ReverseNewtonForwardMain:
            print("Nhập điểm bạn muốn tính nội suy ngược:")
            value = float(input())
            print("Chọn mốc nội suy ngoài cùng bên trái:")
            left = int(input())
            print("Chọn mốc nội suy ngoài cùng bên phải:")
            right = int(input())
            print("Độ chính xác cần đạt:")
            eps = float(input())
            ndataX, ndataY = SliceByHand(dataX,dataY,left, right)
            solanlap, ketqua, hoitu = noiSuyNguoc(ndataX,ndataY,value,eps)
