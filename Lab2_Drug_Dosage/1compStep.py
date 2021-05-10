import numpy as np
from matplotlib import pyplot as plt
import math

# 1 compartment model with step function

dosage=33.333
t_end=24*5
mec=10
mtc=20
step_size=0.001
half_life=22
interval = 8
rb=math.log(2)/half_life
absorbing_fraction=0.12
total_steps= int(t_end/step_size)+1 
quantity_a = np.zeros(total_steps)
quantity_a[0]=absorbing_fraction* dosage
admTime = 0.3333
start = False
counter=admTime/step_size

j=0
for i in range(1,total_steps):
    if(((i)*step_size)%interval ==0):
        start = True
    if start == True and j>=counter :
        j=0
        start= False
    if start==True:
        quantity_a[i-1]+=absorbing_fraction* dosage/ counter
        j+=1
      
    quantity_a[i] = quantity_a[i-1]-rb*quantity_a[i-1]*step_size

x_axis=np.linspace(0,t_end,total_steps)

plt.figure(1)
plt.plot(x_axis,quantity_a,'r' )
plt.legend(['Concentration Of Medicine'])
plt.title('Drug Dosage')
plt.ylabel('Concentration (μg/mL)')
plt.xlabel('Time')
plt.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5,
        alpha = 0.6)
plt.legend(['Conc in Compartment 1'])
plt.axhline(mec,color='y')
plt.axhline(mtc,color='m')
plt.show()
# print(quantity_a[int(48/step_size)])