from DifferentialEquation.eulerForward import mainEulerForward
from DifferentialEquation.eulerBackward import mainEulerBackward
from DifferentialEquation.rectangular import mainRectangular
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

variables = list(sp.symbols("n p"))
t = sp.symbols('t')

deriv_equations = ["e**cos(t)*sin(2*t)","e**sin(t)*cos(t)+1/2"]

vars_start = [0,0]
t_start = 0

h = 0.5

def main(func):
    list_result_t , list_result_var = func(deriv_equations,variables,t,vars_start,t_start,10*np.pi,h)
    array_of_result = np.array(list_result_var).T
    variables_count = len(variables)
    fig, ax = plt.subplots(1,variables_count+1)
    fig.set_size_inches(6*(variables_count+1),6)
    ax[0].plot(*array_of_result, lw = 0.5)
    for i in range(1,variables_count+1) :
        ax[i].plot(list_result_t,array_of_result[i-1])
    return

def test():
    main(mainEulerForward)
    main(mainEulerBackward)
    main(mainRectangular)
    plt.show()

test()