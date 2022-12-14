import pandas as pd
import numpy as np

def NhapDuLieuTho(inputPath, tenDuLieuX, tenDuLieuY):
    if inputPath.endswith(".xlsx"):
        print("File du lieu la file .xlsx (excel).")
        data = pd.read_excel(inputPath)
    if inputPath.endswith(".csv"):
        print("File du lieu la file .csv (comma values)")
        data = pd.read_csv(inputPath)
    print(data)
    dataX = data[tenDuLieuX]
    dataY = data[tenDuLieuY]
    return dataX, dataY

def NhapDuLieuThoDon(inputPath, tenDuLieu):
    if inputPath.endswith(".xlsx"):
        print("File du lieu la file .xlsx (excel).")
        data = pd.read_excel(inputPath)
    if inputPath.endswith(".csv"):
        print("File du lieu la file .csv (comma values)")
        data = pd.read_csv(inputPath)
    dataX = data[tenDuLieu]
    return dataX

def SapXepDuLieuTangDan(dataX: list, dataY: list):
    for i in range(len(dataX)):
        indexMin = i
        for j in range(i + 1, len(dataX)):
            if dataX[j] < dataX[indexMin]:
                indexMin = j
        if indexMin != i:
            dataX[indexMin], dataX[i] = dataX[i], dataX[indexMin]
            dataY[indexMin], dataY[i] = dataY[i], dataY[indexMin]
    return dataX,dataY

def KiemTraDuLieuTrungLap(dataX: list):
    for i in range(0,len(dataX)-1):
        for j in range(i+1, len(dataX)-1):
            if dataX[i] == dataX[j]:
                return True
    return False

def main(inputListOfPointsPath: str,dataXname,dataYname):
    dataX, dataY = NhapDuLieuTho(inputListOfPointsPath,dataXname,dataYname)
    dataX, dataY = SapXepDuLieuTangDan(dataX,dataY)
    repeat = KiemTraDuLieuTrungLap(dataX)
    return dataX, dataY,repeat