def MarkAtCenterLeft(dataX):
    return dataX[int((len(dataX)-1)/2)]

def MarkAtCenterRight(dataX):
    return dataX[int(len(dataX)/2)]

def MarkAtCenter(dataX):
    return (dataX[int((len(dataX)-1)/2)] + dataX[int((len(dataX)-1)/2)+1])/2

def MarkAtStart(dataX):
    return dataX[0]

def MarkAtEnd(dataX):
    return dataX[len(dataX)-1]

def NoMark(dataX):
    return dataX[0]