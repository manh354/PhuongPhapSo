from DifferentialEquation.EulerForward import main as EulerForwardMain
from DifferentialEquation.EulerBackward import main as EulerBackwardMain
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

variables = n,p = list(sp.symbols("n p"))
t = sp.symbols('t')

deriv_equations = ["0.5*n*(1.0-n/200)-0.35*n*p","-0.2*p+0.35*n*p"]

vars_start = [2,2]
t_start = 0

h = 0.1

list_result_t , list_result_var = EulerBackwardMain(deriv_equations,variables,t,vars_start,t_start,2000,h)
ax = plt.figure().add_subplot(2,2)

ax.plot(*np.array(list_result_var).T, lw = 0.5)
plt.show()

def main():
    return