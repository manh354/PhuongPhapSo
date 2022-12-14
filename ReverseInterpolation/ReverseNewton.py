import sys
sys.path.append('../PhuongPhapSo')

from TableAndPolynomial import *
from Newton.NewtonBackward import mainEqui as NewtonBackwardMain
from Newton.NewtonForward import mainEqui as NewtonForwardMain

def mainNewtonForward(dataX, dataY, diemCanNoiSuyNguoc, doChinhXac):
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
    polyTable, _ = NewtonForwardMain(dataX, dataY)
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
    soLanlap = int(1)
    while(abs(t1-t0)>= doChinhXac):
        t0 = t1
        t1 = -CalcPolyReversedInput(iteratePoly,t0)/deltaY0
        print(t1)
        soLanlap += 1
    return soLanlap, t1

solanlap, nghiem = mainNewtonForward([1,2,3,4,5,6,7],[1.1,1.2,1.4,1.8,2.6,4.2,7.4],1.25,10e-5)
print("So lan lap: ")
print(solanlap)
print(nghiem)

_, poly = NewtonForwardMain([1,2,3,4,5,6,7],[1.1,1.2,1.4,1.8,2.6,4.2,7.4])
value = CalcPolyReversedInput(poly, nghiem)
print (value)