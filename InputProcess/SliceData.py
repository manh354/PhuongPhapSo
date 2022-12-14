
def SliceFromTo(dataX, dataY, _from, _to):
    return dataX[_from:_to+1], dataY[_from:_to+1]

def SliceCenterNumber(dataX, dataY, _center, _numberOfPoints):
    return SliceFromTo(dataX, dataY, _center - _numberOfPoints/2,_center+_numberOfPoints/2)