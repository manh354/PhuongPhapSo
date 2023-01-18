import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

adjustable_parameters = sp.symbols("a b")
independent_variable = sp.Symbol("x")

test_function = "5*cos(x) + 0.5*x + 2"
test_function = sp.lambdify(independent_variable,test_function)
fitting_function = "a*x + b"
partial_derivatives = [str(sp.diff(fitting_function, param)) for param in adjustable_parameters]
fitting_function = sp.lambdify([independent_variable,[*adjustable_parameters]],fitting_function, 'numpy')
partial_derivatives = [sp.lambdify([independent_variable,[*adjustable_parameters]],p_d, 'numpy') for p_d in partial_derivatives]
param_start = [1, 0]

dataX = np.linspace(1,100,num = 1000)
truth_dataY = np.array(test_function(dataX))
offsetY = np.multiply(np.add( np.random.rand(len(dataX)),-0.5), 1)
dataY = np.add(truth_dataY, offsetY)


jacobian_matrix = np.array([[p_d(x,param_start) for p_d in partial_derivatives] for x in dataX])
jacobian_matrix_T = jacobian_matrix.T
fitting_function_values = np.array([fitting_function(x,param_start) for x in dataX])
residue_values = np.subtract(dataY, fitting_function_values)
param_iterate_after = np.add(param_start, np.matmul(np.matmul(np.linalg.inv(np.matmul(jacobian_matrix_T, jacobian_matrix)),jacobian_matrix_T),residue_values))
fitting_function_values = np.array([fitting_function(x,param_iterate_after) for x in dataX])
residue_values_new = np.subtract(dataY, fitting_function_values)
while(np.abs(np.sum(residue_values_new - residue_values))< 1e-13):
    residue_values = residue_values_new
    param_iterate_after = np.add(param_start, np.matmul(np.matmul(np.linalg.inv(np.matmul(jacobian_matrix_T, jacobian_matrix)),jacobian_matrix_T),residue_values))
    fitting_function_values = np.array([fitting_function(x,param_iterate_after) for x in dataX])
    residue_values_new = np.subtract(dataY, fitting_function_values)

print(param_iterate_after)
fitted_dataY = [fitting_function(x,param_iterate_after) for x in dataX]
plt.plot(dataX,truth_dataY)
plt.plot(dataX,fitted_dataY)
plt.scatter(dataX,dataY)
plt.show()
