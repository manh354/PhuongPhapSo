import numpy as np

__all__ = ["ConvertXtoT"]

def ConvertXtoT(x,x0,h):
    value = float((x-x0)/h)
    return value

def ConvertXtoU(x,x0,h):
    value = (x-x0)/h - 1/2
    return value