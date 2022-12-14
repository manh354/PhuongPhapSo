import sys
sys.path.append('../PhuongPhapSo')

from TableAndPolynomial import *

# cách chọn chỉ số của Bessel trên bảng sai phân (chẵn số mốc)
#=================================
#   0   1   2   3   4   5   6   7
#=================================
#
#
#
#   -
#   -   -   -
#           -   -   -
#                   -   -   -
#                           -   -
#=================================

def mainBesselNorm(dataX, dataY):
    """
    Tạo đa thức Bessel dạng biến t (chưa qua đổi biến lần 2) . Cần 2n điểm đầu vào
    ---
    Create Bessel polynomial without substituting u = t - 1/2 
    """
    length = len(dataX)
    diffTable = CreateDifferenceTable(dataX,dataY)
    facTable = CreateFactorialTable(length)
    middle = int(len(dataX)/2) #khai bao vị trí giữa
    print(diffTable)
    polyTable = []
    polyTable.append([1])
    if length != 1:
        # đoạn này cần thiết vì thuật toán không xử lý được trường hợp độ dài = 2
        # do phép nhân trong công thức Bessel có tích đa thức dạng (t^2 - t - root^2 + root)
        # chỉ bắt đầu xuất hiện từ số hạng thứ 3
        polyTable.append([-0.5,1]) # thêm đa thức t - 1/2
        if length != 2: # Với đa thức chỉ số lớn hơn 2, ta xử lý như bình thường
            for i in range(2,length):
                if i%2==0:
                    # Các đa thức với hệ số i là chẵn thì cần nhân đa thức bậc chẵn trước nó với đa thức hiệu nghiệm bình phương lệch (t^2 - t - root^2 + root)
                    polyTable.append(MulTwoPoly(polyTable[i-2], CreateRootPolySkewed(int(i/2))))
                else:
                    # Các đa thức với hệ số i là lẻ chỉ cần nhân với đa thức p - 1/2
                    polyTable.append(MulTwoPoly(polyTable[i-1], CreateNewPoly([-0.5,1])))
    for i in range(0, length):
        # đoạn này khai báo vị trí giữa giống Gauss 2
        currentPos = middle+ int(i/2)
        # để hiểu hơn thì có thể xem biểu đồ chọn chỉ số ở trên
        if i%2 == 0:
            # nếu đa thức vị trí i là chẵn thì bị ảnh hưởng bởi 2 hệ số trên bảng sai phân (2 hệ số cộng vào chia đôi)
            polyTable[i] = MulPolyWithCoef(polyTable[i], (diffTable[currentPos,i] + diffTable[currentPos-1,i])/ (2*facTable[i]))
        else:
            # nếu đa thức vị trí i là lẻ thì chỉ bị ảnh hưởng bởi 1 hệ số trên bảng sai phân 
            polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[currentPos,i]/ facTable[i])
    poly = ConvertPolyTableToPoly(polyTable)
    return polyTable, poly



def mainBesselSkewed(dataX, dataY):
    """
    Tạo đa thức Bessel dạng biến u (u = t - 1/2)
    ---
    Create Bessel polynomial by substituting u = t - 1/2 
    """
    length = len(dataX)
    diffTable = CreateDifferenceTable(dataX,dataY)
    facTable = CreateFactorialTable(length)
    middle = int(len(dataX)/2) #khai bao vị trí giữa
    print(diffTable)
    polyTable = []
    polyTable.append([1])
    if length != 1:
        # đoạn này cần thiết vì thuật toán không xử lý được trường hợp độ dài = 2
        # do phép nhân trong công thức Bessel có tích đa thức dạng (u^2 - root^2)
        # chỉ bắt đầu xuất hiện từ số hạng thứ 3
        polyTable.append([0,1]) # thêm đa thức u
        if length != 2: # Với đa thức chỉ số lớn hơn 2, ta xử lý như bình thường
            for i in range(2,length):
                if i%2==0:
                    # Các đa thức với hệ số i là chẵn thì cần nhân đa thức bậc chẵn trước nó với đa thức hiệu nghiệm bình phương (u^2 - root^2)
                    polyTable.append(MulTwoPoly(polyTable[i-2], CreateRootPolySqr((i-1)/2)))
                else:
                    # Các đa thức với hệ số i là lẻ chỉ cần tăng lên 1 bậc so với đa thức bậc chẵn đứng trước nó
                    polyTable.append(CreateChangedPolynomialDegreeByXamount(polyTable[i-1], 1))
    for i in range(0, length):
        # đoạn này khai báo vị trí giữa giống Gauss 2
        currentPos = middle+ int(i/2)
        # để hiểu hơn thì có thể xem biểu đồ chọn chỉ số ở trên
        if i%2 == 0:
            # nếu đa thức vị trí i là chẵn thì bị ảnh hưởng bởi 2 hệ số trên bảng sai phân (2 hệ số cộng vào chia đôi)
            polyTable[i] = MulPolyWithCoef(polyTable[i], (diffTable[currentPos,i] + diffTable[currentPos-1,i])/ (2*facTable[i]))
        else:
            # nếu đa thức vị trí i là lẻ thì chỉ bị ảnh hưởng bởi 1 hệ số trên bảng sai phân 
            polyTable[i] = MulPolyWithCoef(polyTable[i], diffTable[currentPos,i]/ facTable[i])
    poly = ConvertPolyTableToPoly(polyTable)
    return polyTable, poly
