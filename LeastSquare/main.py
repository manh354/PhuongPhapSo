import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

adjustable_parameters = sp.symbols("a1 a2 a3 a4 a5 b1 b2 b3 b4 b5")
independent_variable = sp.Symbol("x")

test_function = "5*cos(x)+4*cos(3*x)+3*cos(5*x)+2*cos(7*x)+1*cos(9*x)"
test_function = sp.lambdify(independent_variable,test_function)
fitting_function = "a1*cos(b1*x)+a2*cos(b2*x)+a3*cos(b3*x)+a4*cos(b4*x)+a5*cos(b5*x)"
partial_derivatives = [str(sp.diff(fitting_function, param)) for param in adjustable_parameters]
fitting_function = sp.lambdify([independent_variable,[*adjustable_parameters]],fitting_function, 'numpy')
partial_derivatives = [sp.lambdify([independent_variable,[*adjustable_parameters]],p_d, 'numpy') for p_d in partial_derivatives]
param_start = [5, 4, 3, 2, 1, 1, 3, 5 ,7 , 5]

dataX = np.linspace(1,15,num = 1000)
truth_dataY = np.array(test_function(dataX))
offsetY = np.multiply(np.add( np.random.rand(len(dataX)),-0.5), 5)
dataY = np.add(truth_dataY, offsetY)


jacobian_matrix = np.array([[p_d(x,param_start) for p_d in partial_derivatives] for x in dataX])
jacobian_matrix_T = jacobian_matrix.T
fitting_function_values = np.array(fitting_function(dataX,param_start))
residue_values = np.subtract(dataY, fitting_function_values)
#print(np.matmul(jacobian_matrix_T,jacobian_matrix))
jjt_1_jt = np.matmul(np.linalg.inv(np.matmul(jacobian_matrix_T, jacobian_matrix)),jacobian_matrix_T)
param_iterate_after = np.add(param_start, np.matmul(jjt_1_jt,residue_values))
fitting_function_values = np.array(fitting_function(dataX,param_start))
residue_values_new = np.subtract(dataY, fitting_function_values)
i = 0
#print(i, residue_values, residue_values_new)
while (np.abs(np.sum(np.subtract(residue_values_new , residue_values)))>= 1e-13) and (i < 100):
    i+= 1
    #print(i, residue_values, residue_values_new)
    residue_values = residue_values_new
    param_iterate_after = np.add(param_start, np.matmul(jjt_1_jt,residue_values))
    fitting_function_values = np.array(fitting_function(dataX,param_start))
    residue_values_new = np.subtract(dataY, fitting_function_values)

print(param_iterate_after)
model_dataX = np.linspace(dataX[0], dataX[-1], num = 1000)
fitted_dataY = [fitting_function(x,param_iterate_after) for x in model_dataX]
plt.plot(model_dataX,fitted_dataY, color = 'orange')
plt.scatter(dataX,dataY)
plt.show()
