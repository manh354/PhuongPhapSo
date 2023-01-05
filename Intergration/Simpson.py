from findStep import main as findStep
import sympy as sp
from sympy import E, sin, cos
import numpy as np
import math
import time

var = sp.Symbol('x') # nhập vào các biến trong phương trình
func = E**(2.5*var) # nhập vào phương trình (đang cố parse sang kiểu numpy để enumerate cho nhanh)
sp_func =  sp.sympify(func) # chuyển hoá string thành dạng phương trình để sympy hiểu được
segment_a = 0 # giá trị bên trái của đoạn
segment_b = 1 # giá trị bên phải của đoạn
eps0 = 5e-8 # giá trị độ chính xác cần đạt

h = findStep(func, var, eps0, segment_a, segment_b, 0.01, 10e-4,1000)
print("Độ lớn của h ban đầu giải ra được: {0}",h)
numSteps = int(math.ceil((segment_b - segment_a)/h)+1)
print("Số bước nhảy kiểu nguyên tính được: {0}", numSteps)
h = (segment_b - segment_a)/numSteps
print("Độ lớn của h sau khi hiệu chỉnh số bước nhảy : {0}", h)

ld_func = sp.lambdify(var, func, "numpy")

list_var = np.linspace(segment_a,segment_b,numSteps)

st = time.time()
for i in range (0,1000):
    test = float(sp_func.subs(var,list_var[0]))
et = time.time()

print("All time: {0}".format(st-et))

st = time.time()
for i in range(0,1000):
    test = float(ld_func(list_var[0]))
et = time.time()

print("All time: {0}".format(st-et))

list_result = [float(sp_func.subs(var,x)) for x in list_var ]
intergrated_list_result = [4*y if i%2 != 0 else 2*y for (i,y) in enumerate(list_result)]

intergrated_list_result[0] = list_result[0]
intergrated_list_result[-1] = list_result[-1]
sum = np.sum(intergrated_list_result)
sum = sum * h/3
print(sum)

new_func = "e**(2.5*x)"
f = sp.lambdify(var, new_func, "numpy")
result = f(list_var)
intergrated_result = [4*y if i%2 != 0 else 2*y for (i,y) in enumerate(result)]
intergrated_result[0] = result[0]
intergrated_result[-1] = result[-1]
print(intergrated_result)
sum = np.sum(intergrated_result)
sum = sum*h/3
print(sum)