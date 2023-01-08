import numpy as np
import sympy as sp

def mainRectangular(symbolic_equation_system : list, symbolic_vars : list[sp.Symbol], symbolic_t : sp.Symbol , vars_start: list[float], t_start: float, t_end: float,h : float):
    list_result_t = []
    list_result_vars = []
    lamdified_equation_system = [sp.lambdify([[*symbolic_vars],symbolic_t],func) for func in symbolic_equation_system]
    vars_iterate = vars_start.copy()
    t_iterate = t_start
    i = 0
    while t_iterate <= t_end:
        equation_system_values = fixedpointIteration(lamdified_equation_system,vars_start, t_iterate,h, 1e-5, 100) # var = var + h * d(var)/dt 
        vars_iterate = np.add(vars_iterate, np.multiply(h,equation_system_values)) # var = var + h * d(var)/dt 
        t_iterate = t_iterate + h
        list_result_t.append(t_iterate)
        list_result_vars.append(vars_iterate)
    return list_result_t,list_result_vars


def fixedpointIteration(lamdified_equation_system ,vars_start : list, t_start, h : float ,epsilon, terminate_threshold):
    vars_iterate = vars_start.copy()
    t_iterate = t_start + h
    equation_system_values_at_start = [equation((vars_iterate),t_start) for equation in lamdified_equation_system]
    equation_system_values_at_iterate = [equation((vars_iterate),t_iterate) for equation in lamdified_equation_system]
    vars_iterate_new = np.add(vars_iterate,np.multiply(0.5*h, np.add(equation_system_values_at_start,equation_system_values_at_iterate)))
    i = 1
    while (np.sum(np.abs(np.subtract(vars_iterate_new, vars_iterate))) >= epsilon) and (i < terminate_threshold):
        equation_system_values_at_iterate = [equation((vars_iterate),t_iterate) for equation in lamdified_equation_system]
        vars_iterate_new = np.add(vars_iterate,np.multiply(0.5*h, np.add(equation_system_values_at_start,equation_system_values_at_iterate)))
        vars_iterate = vars_iterate_new.copy()
        i += 1
    return vars_iterate_new