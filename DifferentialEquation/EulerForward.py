from typing import List
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import time 



def main(symbolic_function_system : list, symbolic_vars : List[sp.Symbol], symbolic_t : sp.Symbol , vars_start: List[float], t_start: float, t_end: float,h : float):
    list_result_t = []
    list_result_vars = []
    lamdified_equation_system = [sp.lambdify([[*symbolic_vars],symbolic_t],func) for func in symbolic_function_system]
    vars_iterate = vars_start.copy()
    t_iterate = t_start
    i = 0
    while t_iterate <= t_end:
        print(i)
        i+= 1
        equation_system_value = [equation((vars_iterate),t_iterate) for equation in lamdified_equation_system]
        vars_iterate = np.add(vars_iterate, np.multiply(h,equation_system_value)) # var = var + h * d(var)/dt 
        t_iterate = t_iterate + h
        list_result_t.append(t_iterate)
        list_result_vars.append(vars_iterate)
    return list_result_t,list_result_vars

def __main__legacy(symbolic_function_system : list, symbolic_vars : List[sp.Symbol], symbolic_t : sp.Symbol , vars_start: List[float], t_start: float, t_end: float,h : float):
    pass