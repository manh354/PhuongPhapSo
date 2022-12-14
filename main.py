from InputProcess.InputIInterface import *

from Langrange.Langrange import main as LangrangeMain
from Newton.NewtonForward import mainAny as NewtonForwardAnyMain
from Newton.NewtonForward import mainEqui as NewtonForwardEquiMain
from Newton.NewtonBackward import mainAny as NewtonBackwardAnyMain
from Newton.NewtonBackward import mainEqui as NewtonBackwardEquiMain

from enum import Enum

def menu1():
    print("Chon PHUONG PHAP ban muon su dung")
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

def menuNewton():
    print("Chon loai phuong phap newton ban muon su dung:")
    print("1: Newton TIEN voi moc bat ki")
    print("2: Newton TIEN voi moc CACH DEU")
    print("3: Newton lui voi moc bat ki")
    print("4: Newton lui voi moc CACH DEU")
    mode = input()
    if(mode == "1"):
        return NewtonForwardAnyMain
    elif(mode == "2"):
        return NewtonForwardEquiMain
    elif(mode == "3"):
        return NewtonBackwardAnyMain
    elif(mode == "4"):
        return NewtonBackwardEquiMain


print("Chon BAI TOAN ban muon giai")
print("1: Noi Suy")
print("2: Noi Suy Nguoc")
print("3: Tinh dao ham")
print("4: Tinh tich phan\n")

char1 = input()
if char1 == "1":
    menu1()
elif char1 == "2":
    print("Chua co!")



