import os
import numpy as np
from matplotlib import pyplot as plt
import numpy
import scipy
import pandas as pd

initial_val1=0.25
initial_val2=0.75
initial_val3=1
initial_val4=1.25
k = 1
t_end=150
step_size=0.01
r=0.05
total_steps= int(t_end/step_size)+1 
quantity_a = np.zeros(total_steps)
quantity_b = np.zeros(total_steps)
quantity_c = np.zeros(total_steps)
quantity_d = np.zeros(total_steps)
quantity_e = np.zeros(total_steps)

quantity_a[0]=initial_val1
quantity_b[0]=initial_val2
quantity_c[0]=initial_val3
quantity_d[0]=initial_val4
quantity_e[0]=0

for i in range(1,total_steps):
    quantity_a[i] = quantity_a[i-1] + r*quantity_a[i-1]*(1 - quantity_a[i-1]/k)*step_size
    quantity_b[i] = quantity_b[i-1] + r*quantity_b[i-1]*(1 - quantity_b[i-1]/k)*step_size
    quantity_c[i] = quantity_c[i-1] + r*quantity_c[i-1]*(1 - quantity_c[i-1]/k)*step_size
    quantity_d[i] = quantity_d[i-1] + r*quantity_d[i-1]*(1 - quantity_d[i-1]/k)*step_size
    quantity_e[i] = quantity_e[i-1] + r*quantity_e[i-1]*(1 - quantity_e[i-1]/k)*step_size
x_axis=np.linspace(0,1,total_steps)
# print(quantity_a[-1])
plt.figure(1)
plt.plot(x_axis,quantity_a,'navy' )
plt.plot(x_axis,quantity_b,'red' )
plt.plot(x_axis,quantity_c,'orange' )
plt.plot(x_axis,quantity_d,'darkgreen' )
plt.plot(x_axis,quantity_e,'m' )
plt.legend(['Initial Population = 0.25','Initial Population = 0.75','Initial Population = 1','Initial Population = 1.25','Initial Population = 0'])
plt.title('Logistic Model')
plt.ylabel('Normalised Population')
plt.xlabel('Time')
plt.grid(b = True, color ='grey',  
        linestyle ='-.', linewidth = 0.5,  
        alpha = 0.6)
plt.show()
