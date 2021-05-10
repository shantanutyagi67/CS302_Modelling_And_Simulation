import os
import numpy as np
from matplotlib import pyplot as plt
import numpy as  np
import scipy
import pandas as pd

# varying r value
b = 0.06 
k = 10 
m = 0.0975
N = 1e7
p = 0.2
u = 0.1
v = 0.04
w = 0.0625


q_values = np.arange(0,0.2,0.05)
count = 1
for q in q_values:
        print(q)
        t_end = 150
        step_size = 1
        total_steps= int(t_end/step_size)+1 

        susceptible = np.zeros(total_steps)
        susceptible_q = np.zeros(total_steps)
        exposed = np.zeros(total_steps)
        exposed_q = np.zeros(total_steps)
        infected_q = np.zeros(total_steps)
        infected_u = np.zeros(total_steps)
        infected_d = np.zeros(total_steps)
        recovered = np.zeros(total_steps)
        death = np.zeros(total_steps)
        total = np.zeros(total_steps)
        N = 10000000
        susceptible[0] = N - 1e4
        infected_u[0] = 1e4

        for i in range(1,total_steps):
                susceptible[i] = susceptible[i-1] + (u*susceptible_q[i-1] - k*q*(1-b)*infected_u[i-1]*susceptible[i-1]/N - k*q*b*infected_u[i-1]*susceptible[i-1]/N - k*(1-q)*b*infected_u[i-1]*susceptible[i-1]/N)*step_size
                susceptible_q[i] = susceptible_q[i-1] + (k*q*(1-b)*infected_u[i-1]*susceptible[i-1]/N - u*susceptible_q[i-1])*step_size
                exposed[i] = exposed[i-1] + (k*(1-q)*b*infected_u[i-1]*susceptible[i-1]/N - p*exposed[i-1])*step_size
                exposed_q[i] = exposed_q[i-1] + (k*q*b*infected_u[i-1]*susceptible[i-1]/N - p*exposed_q[i-1])*step_size
                infected_u[i] = infected_u[i-1] + (p*exposed[i-1] - m*infected_u[i-1] - v*infected_u[i-1] - w*infected_u[i-1])*step_size
                infected_d[i] = infected_d[i-1] + (w*infected_u[i-1] + w*infected_q[i-1] - v*infected_d[i-1] - m*infected_d[i-1])*step_size
                infected_q[i] = infected_q[i-1] + (p*exposed_q[i-1] - m*infected_q[i-1] - v*infected_q[i-1] - w*infected_q[i-1])*step_size
                death[i] = death[i-1] + m*(infected_u[i-1] + infected_q[i-1] + infected_d[i-1])*step_size
                recovered[i] = recovered[i-1] + v*(infected_u[i-1] + infected_q[i-1] + infected_d[i-1])*step_size
        
        x_axis=np.linspace(0,t_end,total_steps)
        net_ill = exposed/N + exposed_q/N + infected_u/N + infected_q/N + infected_d/N
        print(k*b/(v+m+w)*(1-q))

        # plt.plot(x_axis,susceptible/N ,'g--',label='Susceptible')
        # plt.plot(x_axis,susceptible_q/N,'orange',label='Susceptible_Quarantined')
        plt.figure(1)
        plt.plot(x_axis,np.cumsum(net_ill),label='R' +str(count))
        count =count +1
        # plt.plot(x_axis,death/N,'b--',label='Death')
        # plt.plot(x_axis,recovered/N,'m--',label='Recovered')
plt.legend()
plt.grid(b = True, color ='grey',  
linestyle ='-.', linewidth = 0.5,  
alpha = 0.6)
plt.xlabel('Time (in days)')
plt.ylabel('Fraction of population')
plt.title('SARS Model with Varying Reproductionn Number')

        
plt.show()
        