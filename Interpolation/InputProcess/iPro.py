def change(dataZ):
    for i in range(0,len(dataZ)):
        dataZ[i] += 1/38
    return dataZ

import numpy as np

xs = np.linspace(0,1.5,15)
ys = [1+x**2 for x in xs ]
for (i,x) in enumerate(xs):
    print(xs[i],",",ys[i])