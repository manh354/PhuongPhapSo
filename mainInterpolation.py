from Interpolation.InputProcess.InputInterface import main as InputMain
from Interpolation.InputProcess.SliceData import SliceFromTo, AutoSlice, AutoFindSlice, SliceByHand
from Interpolation.valuesConvert import*
from findX0Mode import*

from Interpolation.Langrange.langrange import main as LangrangeMain
from Interpolation.Newton.newtonForward import mainAny as NewtonForwardAnyMain
from Interpolation.Newton.newtonForward import mainEqui as NewtonForwardEquiMain
from Interpolation.Newton.newtonBackward import mainAny as NewtonBackwardAnyMain
from Interpolation.Newton.newtonBackward import mainEqui as NewtonBackwardEquiMain
from Interpolation.Center.bessel import mainNorm as BesselNormMain
from Interpolation.Center.bessel import mainSkewed as BesselSkewedMain
from Interpolation.Center.stirling import main as StirlingMain
from Interpolation.Center.gauss import mainGauss1 as Gauss1Main
from Interpolation.Center.gauss import mainGauss2 as Gauss2Main

from Interpolation.ReverseInterpolation.reverseLangrange import mainReverseLangrange as ReverseLangrangeMain
from Interpolation.ReverseInterpolation.reverseNewton import mainNewtonForwardReverse as ReverseNewtonForwardMain
from Interpolation.ReverseInterpolation.reverseNewton import mainNewtonBackwardReverse as ReverseNewtonBackwardMain
from Interpolation.ReverseInterpolation.monotonicSegments import findUsableSegmentFromData as FindUsableSegment
from Interpolation.tableAndPolynomial import CalcPolyReversedInput


def menuNoisuy():
    print("Chọn PHƯƠNG PHÁP NỘI SUY bạn muốn sử dụng")
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
    print("Chọn loại phương pháp Gauss bạn muốn sử dụng:")
    print("1: Gauss 1 (Chọn bên phải trước, bên trái sau)")
    print("2: Gauss 2 (Chọn bên trái trước, bên phải sau)")
    mode = input()
    if(mode == "1"):
        return Gauss1Main, ConvertXtoT, MarkAtCenterLeft
    return Gauss2Main, ConvertXtoT, MarkAtCenterRight

def menuBessel():
    print("Chọn loại phương pháp NỘI SUY BESSEL bạn muốn sử dụng:")
    print("1: Bessel theo t")
    print("2: Bessel theo u")
    mode = input()
    if(mode == "1"):
        return BesselNormMain, ConvertXtoT, MarkAtCenterLeft
    return BesselSkewedMain, ConvertXtoU, MarkAtCenter

def menuNewton():
    print("Chọn loại phương pháp NỘI SUY NEWTON bạn muốn sử dụng:")
    print("1: Newton tiến với mốc BẤT KÌ")
    print("2: Newton tiến với mốc CÁCH ĐỀU")
    print("3: Newton lùi với mốc BẤT KÌ")
    print("4: Newton lùi với mốc CÁC ĐỀU")
    mode = input()
    if(mode == "1"):
        return NewtonForwardAnyMain, NotConvert, NoMark
    elif(mode == "2"):
        return NewtonForwardEquiMain, ConvertXtoT, MarkAtStart
    elif(mode == "3"):
        return NewtonBackwardAnyMain, NotConvert, NoMark
    return NewtonBackwardEquiMain, ConvertXtoT, MarkAtEnd

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
        noiSuy, conversion, mark = menuNoisuy()
        ## Chọn điểm tính mốc
        print("Chọn điểm bạn muốn tính nội suy:")
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
            dataX, dataY = FindUsableSegment(dataX,dataY, value)
            print("Giá trị bạn muốn tính nội suy ngược là: {0}".format(value))
            print("Tương ứng với mốc này, có đoạn đơn điệu sau:")
            print("X: {0}".format(dataX))
            print("Y: {0}".format(dataY))
            print("Chọn mốc nội suy ngoài cùng bên trái:")
            left = int(input())
            print("Chọn mốc nội suy ngoài cùng bên phải:")
            right = int(input())
            print("Độ chính xác cần đạt:")
            eps = float(input())
            ndataX, ndataY = SliceByHand(dataX,dataY,left, right)
            solanlap, hoitu, ketqua, x, _1 = noiSuyNguoc(ndataX,ndataY,value,eps)
            print("Sau: {0} lần lặp: kết quả theo t là {1} tương đương x = {2}".format(solanlap,ketqua, x))

        if noiSuyNguoc == ReverseNewtonBackwardMain:
            print("Nhập điểm bạn muốn tính nội suy ngược:")
            value = float(input())
            dataX, dataY = FindUsableSegment(dataX,dataY, value)
            print("Giá trị bạn muốn tính nội suy ngược là: {0}".format(value))
            print("Tương ứng với mốc này, có đoạn đơn điệu sau:")
            print("X: {0}".format(dataX))
            print("Y: {0}".format(dataY))
            print("Chọn mốc nội suy ngoài cùng bên trái:")
            left = int(input())
            print("Chọn mốc nội suy ngoài cùng bên phải:")
            right = int(input())
            print("Độ chính xác cần đạt:")
            eps = float(input())
            ndataX, ndataY = SliceByHand(dataX,dataY,left, right)
            solanlap, hoitu, ketqua ,x, _2 = noiSuyNguoc(ndataX,ndataY,value,eps)
            print("Sau: {0} lần lặp: kết quả theo t là {1} tương đương x = {2}".format(solanlap,ketqua, x))

main()