
def SliceFromTo(dataX, dataY, _from, _to):
    return dataX[_from:_to+1], dataY[_from:_to+1]

def SliceCenterNumber(dataX, dataY, _center, _numberOfPoints):
    return SliceFromTo(dataX, dataY, _center - _numberOfPoints/2,_center+_numberOfPoints/2)

def MaxIndexFromCenter(dataX, dataY, _centerValue):
    leftIndex = 0
    rightIndex = 0
    for i in range(0, len(dataX)):
        if(dataX[i] < _centerValue):
            leftIndex += 1
        else:break
    for j in range(len(dataX)-1,0):
        if(dataX[j] > _centerValue):
            rightIndex += 1
        else:break
    if(leftIndex > rightIndex):
        return rightIndex
    return leftIndex

def MaxIndexFromLeftToRight(dataX, dataY, _leftValue):
    leftIndex = 0
    for i in range(0, len(dataX)):
        if(dataX[i] < _leftValue):
            leftIndex += 1
        else:break
    return leftIndex

def MaxIndexFromRightToLeft(dataX, dataY, _leftValue):
    rightIndex = len(dataX)-1
    for j in range(len(dataX)-1,0):
        if(dataX[j] > _leftValue):
            rightIndex -= 1
        else: break
    return rightIndex

def AutoFindSlice(dataX, dataY, Node):
    center = MaxIndexFromCenter(dataX, dataY, Node)
    left = MaxIndexFromLeftToRight(dataX, dataY, Node)
    right = MaxIndexFromRightToLeft(dataX, dataY, Node)
    return left, center,right

def AutoSlice(dataX, dataY, nodeIndex, NumberOfNodesNeeded,mode):
    if(mode == "center"):
        return SliceCenterNumber(dataX,dataY,nodeIndex,NumberOfNodesNeeded)
    if(mode == "left"):
        return SliceFromTo(dataX,dataY,nodeIndex, nodeIndex+NumberOfNodesNeeded)
    if(mode == "right"):
        return SliceFromTo(dataX,dataY, nodeIndex - NumberOfNodesNeeded, nodeIndex)

def SliceByHand(dataX, dataY, leftNodeValue, rightNodeValue):
    leftIndex = 0
    for i in range(0, len(dataX)):
        if(dataX[i] < leftNodeValue):
            leftIndex += 1
        else:break
    rightIndex = len(dataX)-1
    for j in range(len(dataX)-1,0,-1):
        if(dataX[j] > rightNodeValue):
            rightIndex -= 1
        else: break
    return SliceFromTo(dataX,dataY,leftIndex,rightIndex)