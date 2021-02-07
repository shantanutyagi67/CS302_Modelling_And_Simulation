import os
import numpy as np
from matplotlib import pyplot as plt
import numpy
import scipy
import pandas as pd

initial_val1=0.25
initial_val2=0.45
initial_val3=0.55
th = 0.4
k = 1
t_end=100
step_size=0.01
r=0.25
total_steps= int(t_end/step_size)+1 
quantity_a = np.zeros(total_steps)
quantity_b = np.zeros(total_steps)
quantity_c = np.zeros(total_steps)

quantity_a[0]=initial_val1
quantity_b[0]=initial_val2
quantity_c[0]=initial_val3

for i in range(1,total_steps):
    quantity_a[i] = quantity_a[i-1] + r*quantity_a[i-1]*(1 - quantity_a[i-1]/k)*(quantity_a[i-1] - th)*step_size
    quantity_b[i] = quantity_b[i-1] + r*quantity_b[i-1]*(1 - quantity_b[i-1]/k)*(quantity_b[i-1] - th)*step_size
    quantity_c[i] = quantity_c[i-1] + r*quantity_c[i-1]*(1 - quantity_c[i-1]/k)*(quantity_c[i-1] - th)*step_size
    if(quantity_a[i]<=0):
        quantity_a[i]=0
    if(quantity_b[i]<=0):
        quantity_b[i]=0
    if(quantity_c[i]<=0):
        quantity_c[i]=0
x_axis=np.linspace(0,1,total_steps)
# print(quantity_a[-1])
plt.figure(1)
plt.plot(x_axis,quantity_a,'navy' )
plt.plot(x_axis,quantity_b,'red' )
plt.plot(x_axis,quantity_c,'orange' )
plt.axhline(th,color='green')
#plt.axhline(k/2)
#plt.axvline(0)
plt.legend(['Initial Population=0.25','Initial Population=0.45','Initial Population=0.55','Threshold'])
plt.title('Logistic Model with Isolation due to Death')
plt.ylabel('Normalised Population')
plt.xlabel('Time')
plt.grid(b = True, color ='grey',  
        linestyle ='-.', linewidth = 0.5,  
        alpha = 0.6)
plt.show()
