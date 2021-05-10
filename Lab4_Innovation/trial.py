import os
import numpy as np
from matplotlib import pyplot as plt
import numpy
import scipy
import pandas as pd

# air conditioner
# only external influence
initial_val=0.1
q1 = 0.2
q2 = 0.4
t_end=50
na2 = 0.75
na1 = 1
step_size=0.1
total_steps= int(t_end/step_size)+1 
quantity_a = np.zeros(total_steps)
quantity_a1 = np.zeros(total_steps)
quantity_a2 = np.zeros(total_steps)
quantity_a3 = np.zeros(total_steps)
quantity_b = np.zeros(total_steps)
quantity_b1 = np.zeros(total_steps)
quantity_b2 = np.zeros(total_steps)
quantity_b3 = np.zeros(total_steps)

quantity_a[0]=initial_val
quantity_a1[0]=initial_val
quantity_a2[0]=initial_val
quantity_a3[0]=initial_val
quantity_b[0]=initial_val
quantity_b1[0]=initial_val
quantity_b2[0]=initial_val
quantity_b3[0]=initial_val

for i in range(1,total_steps):
    quantity_a[i] = quantity_a[i-1] + (q1*quantity_a[i-1]/na1 )*(na1-quantity_a[i-1])*step_size
    quantity_a1[i] = quantity_a1[i-1] + (q1*quantity_a1[i-1]/na2 )*(na2-quantity_a1[i-1])*step_size
    quantity_a2[i] = quantity_a2[i-1] + (q2*quantity_a2[i-1]/na1 )*(na1-quantity_a2[i-1])*step_size
    quantity_a3[i] = quantity_a3[i-1] + (q2*quantity_a3[i-1]/na2 )*(na2-quantity_a3[i-1])*step_size
    
    quantity_b[i-1] = (q1*quantity_a[i-1]/na1 )*(na1-quantity_a[i-1])
    quantity_b1[i-1] = (q1*quantity_a1[i-1]/na2 )*(na2-quantity_a1[i-1])
    quantity_b2[i-1] = (q2*quantity_a2[i-1]/na1 )*(na1-quantity_a2[i-1])
    quantity_b3[i-1] = (q2*quantity_a3[i-1]/na1 )*(na1-quantity_a3[i-1])

quantity_b[total_steps-1] = quantity_b[total_steps-2] 
quantity_b1[total_steps-1] = quantity_b1[total_steps-2] 
quantity_b2[total_steps-1] = quantity_b2[total_steps-2]
quantity_b3[total_steps-1] = quantity_b3[total_steps-2]

time=quantity_b.argmax(axis=0)
x_axis=np.linspace(0,1,total_steps)

plt.figure(1)
plt.plot(x_axis,quantity_a,'r' )
plt.plot(x_axis,quantity_a1,'r--' )
plt.plot(x_axis,quantity_a2,'b' )
plt.plot(x_axis,quantity_a3,'b--' )

plt.title('Bass Model with external influence')
plt.ylabel('Fraction of Population')
plt.xlabel('Time')
plt.grid(b = True, color ='grey',  
        linestyle ='-.', linewidth = 0.5,  
        alpha = 0.6)
print(time)
plt.legend(['q = 0.2, N = 1','q = 0.2, N = 0.75','q = 0.4, N = 1','q = 0.4, N = 0.75'], loc=2)
plt.show()

plt.figure(2)
plt.plot(x_axis,quantity_b,'r' )
plt.plot(x_axis,quantity_b1,'r--' )
plt.plot(x_axis,quantity_b2,'b' )
plt.plot(x_axis,quantity_b3,'b--' )


plt.title('Bass Model with external influence')
plt.ylabel('Rate of Adoption')
plt.xlabel('Time')
plt.grid(b = True, color ='grey',  
        linestyle ='-.', linewidth = 0.5,  
        alpha = 0.6)
print(time)
plt.legend(['q = 0.2, N = 1','q = 0.2, N = 0.75','q = 0.4, N = 1','q = 0.4, N = 0.75'], loc=2)

plt.xlim(left=0)
plt.show()
print(quantity_b2[quantity_b2.size-1])