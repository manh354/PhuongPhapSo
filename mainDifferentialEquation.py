from DifferentialEquation.eulerForward import mainEulerForward
from DifferentialEquation.eulerBackward import mainEulerBackward
from DifferentialEquation.rectangular import mainRectangular
from DifferentialEquation.rungeKutta import mainRungeKutta4
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

variables = list(sp.symbols("n p"))
t = sp.symbols('t')

deriv_equations =["e**(log(t/10+1)*sin(t))*(sin(t)/(10*(t/10+1))+log(t/10+1)*cos(t))","e**(log(t/10+1)*cos(t))*(cos(t)/(10*(t/10+1))-log(t/10+1)*sin(t))"]
groundtruth_equations = ["e**(log(0.1*t+1)*sin(t))","e**(log(0.1*t+1)*cos(t))"]
vars_start = [1,1]
t_start = 0
h = 0.1

def mainTest2D(func):

    lamdified_equation_system = [sp.lambdify(t,func) for func in groundtruth_equations]
    groundtruth_t = np.linspace(0,10*np.pi,1000)
    groundtruth_var = [[lamdified_equation(t) for t in groundtruth_t] for lamdified_equation in lamdified_equation_system]

    list_result_t , list_result_var = func(deriv_equations,variables,t,vars_start,t_start,10*np.pi,h)
    groundtruth_var_of_sampled_t = np.array([[lamdified_equation(t) for t in list_result_t] for lamdified_equation in lamdified_equation_system])
    array_of_result = np.array(list_result_var).T
    array_of_error = np.abs(np.subtract(groundtruth_var_of_sampled_t,array_of_result))
    error_of_2d_graph = np.sqrt(np.add(
        np.square(array_of_error[0]),
        np.square(array_of_error[1])))
    variables_count = len(variables)
    fig, ax = plt.subplots(2,variables_count+1)
    fig.set_size_inches(6*(variables_count+1),12)
    ax[0,0].plot(*array_of_result)
    ax[1,0].plot(list_result_t,error_of_2d_graph)
    ax[0,0].plot(groundtruth_var[0],groundtruth_var[1])
    for i in range(1,variables_count+1) :
        ax[0,i].plot(list_result_t,array_of_result[i-1])
        ax[1,i].plot(list_result_t,array_of_error[i-1])
        ax[0,i].plot(groundtruth_t,groundtruth_var[i-1])
    return

def test():
    
    mainTest2D(mainEulerForward)
    mainTest2D(mainEulerBackward)
    mainTest2D(mainRectangular)
    mainTest2D(mainRungeKutta4)
    plt.show()

test()