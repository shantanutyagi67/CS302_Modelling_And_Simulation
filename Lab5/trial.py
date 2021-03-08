import os
import numpy as np
from matplotlib import pyplot as plt
import numpy as  np
import scipy
import pandas as pd

#
b = 0.06 
m = 0.0975
N = 1e7
p = 0.2
u = 0.1
v = 0.04
w = 0.0625
#q_value= 0.15
k=10

r = k*b/(v+m+w)
# print(r)
r_int = [0.5 ,1.0 ,1.5 ,2.0, 2.5 ]
d_frac = [i/r for i in r_int]
q_values = np.linspace(0,1,100)

for i in r_int:
        d_value = np.zeros(100)
        count = 0
        for q in range(len(q_values)):
                d_value[q] = max(0,1 - i/(r*(1-q_values[q])))
                if d_value[q] == 0:
                        count = q
                        break
        plt.plot(q_values[0:count+1],d_value[0:count+1],label='r_int = '+str(i))
        plt.legend()
plt.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.6)
plt.xlabel('q')
plt.ylabel('1 - Dint/D')
plt.title('title' )
plt.show()