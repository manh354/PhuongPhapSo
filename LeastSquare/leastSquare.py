import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


#dataX=np.array([0.038,0.194,0.425,0.626,1.253,2.500,3.740])
#dataY=np.array([0.050,0.127,0.094,0.2122,0.2729,0.2665,0.3317])

adjustable_parameters = sp.symbols("a b c")
independent_variable = sp.Symbol("x")
test_function = "5*cos(x) + 0.5*x + 2"
fitting_function = "a*cos(x) + b*x + c"
param_start = [1,0,0]

test_function = sp.lambdify(independent_variable,test_function)
partial_derivatives = [str(sp.diff(fitting_function, param)) for param in adjustable_parameters]
print(partial_derivatives)
fitting_function = sp.lambdify([independent_variable,[*adjustable_parameters]],fitting_function, 'numpy')
partial_derivatives = [sp.lambdify([independent_variable,[*adjustable_parameters]],p_d, 'numpy') for p_d in partial_derivatives]

dataX = np.linspace(1,3,num = 100)
truth_dataY = np.array(test_function(dataX))
maxY = np.max(np.abs(truth_dataY))
offsetY = np.multiply(np.add( np.random.normal(0,1,len(dataX)),0), 0.1*maxY)
dataY = np.add(truth_dataY, offsetY)


fitting_function_values = np.array(fitting_function(dataX,param_start))
residue_values = np.subtract(dataY, fitting_function_values)

jacobian_matrix = np.array([[p_d(x,param_start) for p_d in partial_derivatives] for x in dataX])
jacobian_matrix_T = jacobian_matrix.T
#print(np.matmul(jacobian_matrix_T,jacobian_matrix))
jjt_1_jt = np.matmul(np.linalg.inv(np.matmul(jacobian_matrix_T, jacobian_matrix)),jacobian_matrix_T)
param_iterate_after = np.add(param_start, np.matmul(jjt_1_jt,residue_values))
fitting_function_values = np.array(fitting_function(dataX,param_iterate_after))
residue_values_new = np.subtract(dataY, fitting_function_values)
i = 1
print("lần lặp thứ :", i)
print(*["{0} = {1};".format(adjustable_parameters[i],x) for (i,x) in enumerate(param_iterate_after)])
while (np.abs(np.sum(np.subtract(residue_values_new , residue_values)))>= 0.005) and (i < 100):
    i+= 1
    residue_values = residue_values_new
    jacobian_matrix = np.array([[p_d(x,param_iterate_after) for p_d in partial_derivatives] for x in dataX])
    jacobian_matrix_T = jacobian_matrix.T
    jjt_1_jt = np.matmul(np.linalg.inv(np.matmul(jacobian_matrix_T, jacobian_matrix)),jacobian_matrix_T)
    param_iterate_after = np.add(param_iterate_after, np.matmul(jjt_1_jt,residue_values))
    fitting_function_values = np.array(fitting_function(dataX,param_iterate_after))
    residue_values_new = np.subtract(dataY, fitting_function_values)
    print("lần lặp thứ :", i)
    print(*["{0} = {1};".format(adjustable_parameters[i],x) for (i,x) in enumerate(param_iterate_after)])

model_dataX = np.linspace(dataX[0], dataX[-1], num = 1000)
fitted_dataY = [fitting_function(x,param_iterate_after) for x in model_dataX]
plt.plot(model_dataX,fitted_dataY, color = 'orange')
plt.scatter(dataX,dataY)
plt.show()
