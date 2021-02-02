import os
import numpy as np
from matplotlib import pyplot as plt
import numpy
import scipy
import pandas as pd

initial_val=0.75
k = 1
e = 0.25
t_end=50*2
step_size=0.1
r=0.5
total_steps= int(t_end/step_size)+1 
quantity_a = np.zeros(total_steps)
quantity_b = np.zeros(total_steps)
quantity_c = np.zeros(total_steps)

quantity_a[0]=initial_val
quantity_b[0]=initial_val
quantity_c[0]=initial_val

h1 = r*k/4 + 0.1
h2 = r*k/4
h3 = r*k/4 - 0.01

for i in range(1,total_steps):
    # quantity_a[i] = quantity_a[i-1] + (r*quantity_a[i-1]*(1 - quantity_a[i-1]/k)-h1)*step_size
    quantity_b[i] = quantity_b[i-1] + (r*quantity_b[i-1]*(1 - quantity_b[i-1]/k)-e*quantity_b[i-1])*step_size
    #quantity_c[i] = quantity_c[i-1] + (r*quantity_c[i-1]*(1 - quantity_c[i-1]/k)-e*quantity_b[i-1])*step_size
# print(quantity_a[-1])
x_axis=np.linspace(0,1,total_steps)
plt.figure(1)
# plt.plot(x_axis,quantity_a,'navy' )
plt.plot(x_axis,quantity_b,'red' )
#plt.plot(x_axis,quantity_c,'orange' )
plt.legend(['h=4h/k','h<4h/k'])
plt.title('Constant-Rate Harvesting')
plt.ylabel('Normalised Population')
plt.xlabel('Time')
plt.grid(b = True, color ='grey',  
        linestyle ='-.', linewidth = 0.5,  
        alpha = 0.6)
plt.axhline(0.5)
plt.show()
