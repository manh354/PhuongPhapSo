import sys
sys.path.append('../PhuongPhapSo')

import math

from Interpolation.TableAndPolynomial import *
from Interpolation.Newton.NewtonBackward import mainEqui as mainNewtonBackward
from Interpolation.Newton.NewtonForward import mainEqui as mainNewtonForward

def mainNewtonForwardReverse(dataX, dataY, diemCanNoiSuyNguoc, doChinhXac):
    """
    Hàm nội suy ngược newton
    
    Params:
        dataX: đầu vào X
        dataY: đầu vào Y
        diemCanNoiSuyNguoc: điểm cần nội suy ngược
        doChinhXac: độ chính xác cần đạt (sẽ tính 2 lần lặp liên tiếp mà độ lớn hiệu không vượt quá giá trị này)
    
    Return:
        Trả về giá trị là vị trí của t (phải convert ngược lại ra giá trị x)
    """
    polyTable, _ = mainNewtonForward(dataX, dataY)
    # Đoạn này ta tạo đa thức lặp Phi (t) lặp bằng cách chuyển vế, chuyển số hạng bậc 1 chứa t sang vế trái và chuyển y_ (giá trị nội suy cần tính) sang vế phải
    y0 = polyTable[0][0]
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Đoạn này để tiết kiệm tính toán, trước hết đặt dấu trừ ra ngoài toàn bộ công thức vế phải
    # nên hệ số của đa thức đầu tiên nhận giá trị y0 - y_
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    polyTable[0][0] = y0 - diemCanNoiSuyNguoc
    deltaY0 = polyTable[1][1] # lấy delta y0 ra để dùng chia đa thức sau (xem công thức lặp newton)
    polyTable[1][1] = 0 # tương đương với việc chuyển số hạng bậc 1 sang vế trái nên vế phải không còn số hạng t bậc 1

    iteratePoly = ConvertPolyTableToPoly(polyTable)

    # để bắt đầu lặp, ta cần gán cho t0 giá trị ban đầu, lấy bằng (y_ - y0)/delta y0
    t0 = -polyTable[0][0]/deltaY0 # vừa tính ở trên : polyTable[0][0] = y0 - y_
    print(t0)
    t1 = -CalcPolyReversedInput(iteratePoly,t0)/deltaY0 # tính lần lặp đầu
    print(t1)
    soLanLap = int(1)
    hoiTuHayKhong = True
    while(abs(t1-t0)>= doChinhXac):
        t0 = t1
        t1 = -CalcPolyReversedInput(iteratePoly,t0)/deltaY0
        if(math.isinf(t1)):
            hoiTuHayKhong = False
            print("Gia tri ra VO CUNG")
            break
        if(soLanLap > 1000):
            hoiTuHayKhong = False
            print("Gia tri khong hoi tu")
            break
        soLanLap += 1
        print("Lan lap thu:{0}; gia tri t{0} = {1}".format(soLanLap,t1))
    return soLanLap, hoiTuHayKhong, t1


def mainNewtonBackward(dataX, dataY, diemCanNoiSuyNguoc, doChinhXac):
    polyTable, _ = mainNewtonBackward(dataX, dataY)
    # Đoạn này ta tạo đa thức lặp Phi (t) lặp bằng cách chuyển vế, chuyển số hạng bậc 1 chứa t sang vế trái và chuyển y_ (giá trị nội suy cần tính) sang vế phải
    y0 = polyTable[0][0]
    print(y0)
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Đoạn này để tiết kiệm tính toán, trước hết đặt dấu trừ ra ngoài toàn bộ công thức vế phải
    # nên hệ số của đa thức đầu tiên nhận giá trị y0 - y_
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    polyTable[0][0] = y0 - diemCanNoiSuyNguoc
    deltaY0 = polyTable[1][1] # lấy delta y0 ra để dùng chia đa thức sau (xem công thức lặp newton)
    polyTable[1][1] = 0 # tương đương với việc chuyển số hạng bậc 1 sang vế trái nên vế phải không còn số hạng t bậc 1

    iteratePoly = ConvertPolyTableToPoly(polyTable)

    # để bắt đầu lặp, ta cần gán cho t0 giá trị ban đầu, lấy bằng (y_ - y0)/delta y0
    t0 = -polyTable[0][0]/deltaY0 # vừa tính ở trên : polyTable[0][0] = y0 - y_
    t1 = -CalcPolyReversedInput(iteratePoly,t0)/deltaY0 # tính lần lặp đầu
    soLanLap = int(1)
    print("Lan lap thu:{0}; gia tri t{0} = {1}".format(soLanLap,t1))
    hoiTuHayKhong = True
    while(abs(t1-t0)>= doChinhXac):
        t0 = t1
        t1 = -CalcPolyReversedInput(iteratePoly,t0)/deltaY0
        if(math.isinf(t1)):
            hoiTuHayKhong = False
            print("Gia tri ra VO CUNG")
            break
        if(soLanLap > 1000):
            hoiTuHayKhong = False
            print("Gia tri khong hoi tu")
            break
        soLanLap += 1
        print("Lan lap thu:{0}; gia tri t{0} = {1}".format(soLanLap,t1))
    return soLanLap, hoiTuHayKhong, t1

def findMonotonicSegments(dataX, dataY):
    resultX = []
    resutlY = []
    # Nếu dộ dài của data nhỏ hơn bằng 2 thì chắc chắn chúng ở trong 1 khoảng đơn điệu
    # trong trường hợp data dài hơn, ta xét dấu giữa 2 phần tử
    # nếu giữa hai phần tử đổi dấu => sinh ra 2 khoảng đơn điệu tương ứng.
    if(len(dataX) <= 2 | len(dataY) <=2):
        resultX = [dataX]
        resutlY = [dataY]
        return resultX,resutlY
    sign = 1 if dataY[1] - dataY[0] > 0 else -1
    monotonicX = [dataX[0], dataX[1]]
    monotonicY = [dataY[0], dataY[1]]
    for i in range(2,len(dataY)):
        if i == len(dataY)-1:
            resultX.append(monotonicX)
            resutlY.append(monotonicY)
        if sign*(dataY[i] - dataY[i-1]) >= 0:
            monotonicX.append(dataX[i])
            monotonicY.append(dataY[i])
        else:
            sign = -sign
            resultX.append(monotonicX)
            resutlY.append(monotonicY)
            monotonicX = [dataX[i-1],dataX[i]]
            monotonicY = [dataY[i-1],dataY[i]]
    return resultX,resutlY

print(findMonotonicSegments([1,0,1,3,4,52,1,0,-1,-2,-3,-4],[1,0,1,3,4,52,1,0,-1,-2,-3,-4])[0])