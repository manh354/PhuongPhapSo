from DifferentialEquation.eulerForward import mainEulerForward
from DifferentialEquation.eulerBackward import mainEulerBackward
from DifferentialEquation.trapezoid import mainTrapezoid
from DifferentialEquation.rungeKutta import mainRungeKutta4_Classic, mainRungaKutta3_Heun
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

variables = list(sp.symbols("x y"))
t = sp.symbols('t')

deriv_equations = ["cos(2*t)**2*x","sin(t)**2*y"]
groundtruth_equations=["e**((sin(4*t)+4*t)/8)","e**(t/2-sin(2*t)/4)"]
vars_start = [1,1]
t_start = 0
t_end = 5
h = 0.5

def main2D(func):

    list_result_t , list_result_var = func(deriv_equations,variables,t,vars_start,t_start,t_end,h)
    array_of_result = np.array(list_result_var).T
    variables_count = len(variables)
    fig, ax = plt.subplots(1,variables_count+1)
    fig.set_size_inches(6*(variables_count+1),6)
    ax[0].plot(*array_of_result)
    for i in range(1,variables_count+1) :
        ax[i].plot(list_result_t,array_of_result[i-1])
    return

def mainTest2D(func):

    lamdified_equation_system = [sp.lambdify(t,func) for func in groundtruth_equations]
    groundtruth_t = np.linspace(t_start,t_end,1000)
    groundtruth_var = [[lamdified_equation(t) for t in groundtruth_t] for lamdified_equation in lamdified_equation_system]

    list_result_t , list_result_var = func(deriv_equations,variables,t,vars_start,t_start,t_end,h)
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
    print("Euler hiện: ")
    print("=============================================================================")
    mainTest2D(mainEulerForward)
    plt.show()
    print("Euler ẩn: ")
    print("=============================================================================")
    mainTest2D(mainEulerBackward)
    plt.show()
    print("Thang ẩn: ")
    print("=============================================================================")
    mainTest2D(mainTrapezoid)
    plt.show()
    print("RK3 Heun: ")
    print("=============================================================================")
    mainTest2D(mainRungaKutta3_Heun)
    plt.show()
    print("RK4 Cổ điển: ")
    print("=============================================================================")
    mainTest2D(mainRungeKutta4_Classic)
    plt.show()

def solve():
    main2D(mainEulerForward)
    main2D(mainEulerBackward)
    main2D(mainTrapezoid)
    main2D(mainRungaKutta3_Heun)
    main2D(mainRungeKutta4_Classic)
    plt.show()

test()