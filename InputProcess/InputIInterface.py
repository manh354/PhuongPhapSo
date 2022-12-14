import pandas as pd
import numpy as np

def NhapDuLieuTho(inputPath):
    if inputPath.endswith(".xlsx"):
        print("File du lieu la file .xlsx (excel).")
        data = pd.read_excel(inputPath)
    if inputPath.endswith(".csv"):
        print("File du lieu la file .csv (comma values)")
        data = pd.read_csv(inputPath)
    dataX = data['x']
    dataY = data['y']
    return dataX, dataY

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

def main(inputPath: str):
    dataX, dataY = NhapDuLieuTho(inputPath)
    dataX, dataY = SapXepDuLieuTangDan(dataX,dataY)
    repeat = KiemTraDuLieuTrungLap(dataX)
    return dataX, dataY, repeat