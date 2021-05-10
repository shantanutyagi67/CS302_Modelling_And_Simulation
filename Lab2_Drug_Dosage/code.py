import numpy as np
from matplotlib import pyplot as plt
import math

initial_val=33.333
t_end=24*1
mec=10
mtc=20
step_size=0.001
half_life=22
interval = 5
rb=math.log(2)/half_life
ra=2*rb
absorbing_fraction=0.12
total_steps= int(t_end/step_size)+1 
quantity_a = np.zeros(total_steps)
quantity_b = np.zeros(total_steps)
quantity_a[0]=absorbing_fraction* initial_val
dosage=100

for i in range(1,total_steps):
    if(((i)*step_size)%interval == 0):
        quantity_a[i-1]+=absorbing_fraction* dosage
    quantity_a[i] = quantity_a[i-1]-ra*quantity_a[i-1]*step_size
    quantity_b[i] = quantity_b[i-1] + (ra*quantity_a[i-1] - rb*quantity_b[i-1])*step_size

x_axis=np.linspace(0,t_end,total_steps)

plt.figure(1)
plt.plot(x_axis,quantity_a,'r' )
plt.plot(x_axis,quantity_b,'g')
plt.legend(['Concentration Of Medecine'])
plt.title('Drug Dosage')
plt.ylabel('Concentration (μg/mL)')
plt.xlabel('Time')
plt.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5,
        alpha = 0.6)
plt.legend(['Compartment 1','Compartment 2'])
plt.axhline(mec,color='y')
plt.axhline(mtc,color='m')
plt.show()