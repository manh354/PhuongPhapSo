from Interpolation.InputProcess.InputInterface import main as InputMain
from Interpolation.InputProcess.SliceData import SliceFromTo, AutoSlice, AutoFindSlice, SliceByHand
from Interpolation.valuesConvert import*
from findX0Mode import*

from Interpolation.Langrange.langrange import wrapperLangrange as LangrangeMain
from Interpolation.Newton.newtonForward import wrapperNewtonForwardAny as NewtonForwardAnyMain
from Interpolation.Newton.newtonForward import wrapperNewtonForwardEqui as NewtonForwardEquiMain
from Interpolation.Newton.newtonBackward import wrapperNewtonBackwardAny as NewtonBackwardAnyMain
from Interpolation.Newton.newtonBackward import wrapperNewtonBackwardEqui as NewtonBackwardEquiMain
from Interpolation.Center.bessel import wrapperBesselNorm as BesselNormMain
from Interpolation.Center.bessel import wrapperBesselSkewed as BesselSkewedMain
from Interpolation.Center.stirling import wrapperStirling as StirlingMain
from Interpolation.Center.gauss import wrapperGauss1 as Gauss1Main
from Interpolation.Center.gauss import wrapperGauss2 as Gauss2Main

from Interpolation.ReverseInterpolation.reverseLangrange import mainReverseLangrange as ReverseLangrangeMain
from Interpolation.ReverseInterpolation.reverseNewton import mainNewtonForwardReverse as ReverseNewtonForwardMain
from Interpolation.ReverseInterpolation.reverseNewton import mainNewtonBackwardReverse as ReverseNewtonBackwardMain
from Interpolation.ReverseInterpolation.monotonicSegments import findUsableSegmentFromData as FindUsableSegment
from Interpolation.tableAndPolynomial import CalcPolyReversedInput

import matplotlib.pyplot as plt
import numpy as np

def menuNoisuy():
    print("Chọn PHƯƠNG PHÁP NỘI SUY bạn muốn sử dụng")
    print("1: Langrange")
    print("2: Newton")
    print("3: Gauss")
    print("4: Bessel")
    print("5: Stirling")
    mode = input()
    if(mode == "1"):
        return LangrangeMain
    elif(mode == "2"):
        return menuNewton()
    elif(mode == "3"):
        return menuGauss()
    elif(mode == "4"):
        return menuBessel()
    return StirlingMain


def menuGauss():
    print("Chọn loại phương pháp Gauss bạn muốn sử dụng:")
    print("1: Gauss 1 (Chọn bên phải trước, bên trái sau)")
    print("2: Gauss 2 (Chọn bên trái trước, bên phải sau)")
    mode = input()
    if(mode == "1"):
        return Gauss1Main
    return Gauss2Main

def menuBessel():
    print("Chọn loại phương pháp NỘI SUY BESSEL bạn muốn sử dụng:")
    print("1: Bessel theo t (bên trái)")
    print("2: Bessel theo t - 1/2 (ở giữa)")
    mode = input()
    if(mode == "1"):
        return BesselNormMain
    return BesselSkewedMain

def menuNewton():
    print("Chọn loại phương pháp NỘI SUY NEWTON bạn muốn sử dụng:")
    print("1: Newton tiến với mốc BẤT KÌ")
    print("2: Newton tiến với mốc CÁCH ĐỀU")
    print("3: Newton lùi với mốc BẤT KÌ")
    print("4: Newton lùi với mốc CÁC ĐỀU")
    mode = input()
    if(mode == "1"):
        return NewtonForwardAnyMain
    elif(mode == "2"):
        return NewtonForwardEquiMain
    elif(mode == "3"):
        return NewtonBackwardAnyMain
    return NewtonBackwardEquiMain

def menuNoisuyNguoc():
    print("Chọn phương pháp NỘI SUY NGƯỢC bạn muốn sử dụng:")
    print("1: Langrange ngược")
    print("2: Lặp Newton xuôi")
    print("3: Lặp Newton ngược")
    mode = input()
    if(mode == "1"):
        return ReverseLangrangeMain
    elif (mode == "2"):
        return ReverseNewtonForwardMain
    return ReverseNewtonBackwardMain

############################### Main program ##################################
def main():
    listOfPointsPath = "inputData.csv"
    interpolatePoint = "inputPoint.csv"
    sliceMode = "tay"
    ### kiểm tra đầu vào
    dataX, dataY, CoBiTrungLapKhong, CoCachDeuNhauKhong = InputMain(listOfPointsPath,'x','y')
    if(CoBiTrungLapKhong):
        print("Dữ liệu bị TRÙNG LẶP... chưa xử lý được!")
        exit()
    print("Dữ liệu hợp lý, tiếp tục xử lý.")
    h = dataX[1] - dataX[0]
    if(CoCachDeuNhauKhong):
        print("Dữ liệu CÁCH ĐỀU nhau")
    else:
        print("Dữ liệu KHÔNG CÁCH ĐỀU nhau")

    print("Bạn muốn chọn dữ liệu trong khoảng nào?")

    print("Chọn BÀI TOÁN bạn muốn giải")
    print("1: Nội suy")
    print("2: Nội suy ngược")
    print("3: Tính đạo hàm")
    print("4: Tính tích phân\n")

    char1 = input()

    if char1 == "1":
        noiSuy = menuNoisuy()
        ## Chọn điểm tính mốc
        print("Chọn điểm bạn muốn tính nội suy:")
        value = float(input())
        ## Xử lý nội suy
        noiSuy(dataX, dataY,value)

    elif char1 == "2":
        noiSuyNguoc = menuNoisuyNguoc()

        if noiSuyNguoc == ReverseLangrangeMain:
            print("Nhập điểm bạn muốn tính nội suy ngược:")
            value = float(input())
            dataX, dataY = FindUsableSegment(dataX,dataY, value)
            print("Giá trị bạn muốn tính nội suy ngược là: {0}".format(value))
            print("Tương ứng với mốc này, có đoạn đơn điệu sau:")
            print("X: {0}".format(dataX))
            print("Y: {0}".format(dataY))
            _, _,polyTable,poly = noiSuyNguoc(dataX, dataY, value)


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
            solanlap, hoitu, ketqua, x= noiSuyNguoc(ndataX,ndataY,value,eps)
            print("Sau: {0} lần lặp: kết quả theo t là {1} tương đương x = {2}".format(solanlap,ketqua, x))

        if noiSuyNguoc == ReverseNewtonBackwardMain:
            print("Nhập điểm bạn muốn tính nội suy ngược:")
            value = float(input())
            print("Chọn mốc nội suy ngoài cùng bên trái:")
            left = int(input())
            print("Chọn mốc nội suy ngoài cùng bên phải:")
            right = int(input())
            print("Độ chính xác cần đạt:")
            eps = float(input())
            ndataX, ndataY = SliceByHand(dataX,dataY,left, right)
            solanlap, hoitu, ketqua ,x= noiSuyNguoc(ndataX,ndataY,value,eps)
            print("Sau: {0} lần lặp: kết quả theo t là {1} tương đương x = {2}".format(solanlap,ketqua, x))


main()