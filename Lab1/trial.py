import os
import numpy as np
from matplotlib import pyplot as plt
import numpy
import scipy


intial_val=10
t_end=100
step_size=0.001
rb=0.1
ra=0.1
total_steps= int(t_end/step_size)+1 

# print(total_steps)
quantity_a = np.zeros(total_steps)
quantity_b = np.zeros(total_steps)
quantity_c = np.zeros(total_steps)
quantity_d= np.zeros(total_steps)
quantity_a[0]=intial_val
quantity_d[0]=quantity_a[0]

for i in range(1,total_steps):
    quantity_a[i] = quantity_a[i-1]-ra*quantity_a[i-1]*step_size
    quantity_b[i] = quantity_b[i-1] + (ra*quantity_a[i-1] - rb*quantity_b[i-1])*step_size
    quantity_c[i] = quantity_c[i-1] + rb*quantity_b[i-1]*step_size
    quantity_d[i]=quantity_a[i]+quantity_b[i]+quantity_c[i]

x_axis=np.linspace(0,t_end,total_steps)
print(x_axis.shape)
plt.figure(1)
plt.plot(x_axis,quantity_a/intial_val,'r' )
plt.plot(x_axis,quantity_b/intial_val,'g' )
plt.plot(x_axis, quantity_c/intial_val,'b')
plt.plot(x_axis, quantity_d/intial_val,'y')
plt.title('Radioactive Decay')
plt.ylabel('Number')
plt.xlabel('Time')
plt.grid()
plt.show()
