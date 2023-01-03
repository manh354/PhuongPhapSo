import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

variables = list(sp.symbols("x y z"))
t = sp.symbols('t')

deriv_equations = ["sin(x**t*z)*y*x*z","sin(t*x*y)","-cos(t^2*z)"]
vars_start = [0.5,1,-1.2]
t_start = 0

h = 0.1

simpifyEquation = [sp.sympify(x) for x in deriv_equations]
t_iterate = t_start
vars_iterate = vars_start

list_t = [t_start]
list_vars = [vars_iterate]

for i in range(0,100):
    print(i)
    subtituteList = list(zip(variables,vars_iterate))+[(t,t_iterate)]
    funcs_iterate = [x.subs(subtituteList) for x in simpifyEquation]
    vars_iterate = np.add(vars_iterate, np.multiply(h, funcs_iterate))
    t_iterate = t_iterate + h
    list_t.append(t_iterate)
    list_vars.append(vars_iterate)

for i in range(0,len(variables)):
    print(i)
    plt.subplot(1,len(variables),i+1)
    list_var_i = [x[i] for x in list_vars]
    plt.plot(list_t,list_var_i)
plt.show()