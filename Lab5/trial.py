import os
import numpy as np
from matplotlib import pyplot as plt
import numpy as  np
import scipy
import pandas as pd

b = 0.06 
k = 10 
m = 0.0975
N = 1e7
p = 0.2
u = 0.1
v = 0.04
w = 0.0625

# def s(u,k,q,b,v,w,m,p,S,Sq,E,Eq,Iq,Iu,Id,D,R,N):
#         return u*Sq - k*q*(1-b)*Iu*S/N - k*q*Iu*S/N - k*(1-q)*b*Iu*S/N
# def sq(u,k,q,b,v,w,m,p,S,Sq,E,Eq,Iq,Iu,Id,D,R,N):
#         return k*q*(1-b)*Iu*S/N - u*Sq
# def e(u,k,q,b,v,w,m,p,S,Sq,E,Eq,Iq,Iu,Id,D,R,N):
#         return k*(1-q)*b*Iu*S/N - p*E
# def eq(u,k,q,b,v,w,m,p,S,Sq,E,Eq,Iq,Iu,Id,D,R,N):
#         return k*q*b*Iu*S/N - p*Eq
# def iu(u,k,q,b,v,w,m,p,S,Sq,E,Eq,Iq,Iu,Id,D,R,N):
#         return p*E - m*Iu - v*Iu - w*Iu
# def iq(u,k,q,b,v,w,m,p,S,Sq,E,Eq,Iq,Iu,Id,D,R,N):
#         return p*Eq - m*Iq - v*Iq - w*Iq
# def ids(u,k,q,b,v,w,m,p,S,Sq,E,Eq,Iq,Iu,Id,D,R,N):
#         return w*Iu + w*Iq - v*Id - m*Id
# def d(u,k,q,b,v,w,m,p,S,Sq,E,Eq,Iq,Iu,Id,D,R,N):
#         return m*(Iu + Iq + Id)
# def r(u,k,q,b,v,w,m,p,S,Sq,E,Eq,Iq,Iu,Id,D,R,N):
#         return v*(Iu + Iq + Id)

q_values = np.arange(0,0.2,0.05)

for q in q_values:
        
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
                #         return u*Sq - k*q*(1-b)*Iu*S/N - k*q*Iu*S/N - k*(1-q)*b*Iu*S/N

                susceptible[i] = susceptible[i-1] + (u*susceptible_q[i-1] - k*q*(1-b)*infected_u[i-1]*susceptible[i-1]/N - k*q*infected_u[i-1]*susceptible[i-1]/N - k*(1-q)*b*infected_u[i-1]*susceptible[i-1]/N)*step_size
                susceptible_q[i] = susceptible_q[i-1] + (k*q*(1-b)*infected_u[i-1]*susceptible[i-1]/N - u*susceptible_q[i-1])*step_size
                exposed[i] = exposed[i-1] + (k*(1-q)*b*infected_u[i-1]*susceptible[i-1]/N - p*exposed[i-1])*step_size
                exposed_q[i] = exposed_q[i-1] + (k*q*b*infected_u[i-1]*susceptible[i-1]/N - p*exposed_q[i-1])*step_size
                infected_u[i] = infected_u[i-1] + (p*exposed[i-1] - m*infected_u[i-1] - v*infected_u[i-1] - w*infected_u[i-1])*step_size
                infected_d[i] = infected_d[i-1] + (w*infected_u[i-1] + w*infected_q[i-1] - v*infected_d[i-1] - m*infected_d[i-1])*step_size
                infected_q[i] = infected_q[i-1] + (p*exposed[i] - m*infected_q[i-1] - v*infected_q[i-1] - w*infected_q[i-1])*step_size
                death[i] = death[i-1] + m*(infected_u[i-1] + infected_q[i-1] + infected_d[i-1])*step_size
                recovered[i] = recovered[i-1] + v*(infected_u[i-1] + infected_q[i-1] + infected_d[i-1])*step_size
        x_axis=np.linspace(0,t_end,total_steps)

        plt.plot(x_axis,susceptible/N,label='S',color='green')
        plt.plot(x_axis,susceptible_q/N,label='Sq',color='blue')
        plt.plot(x_axis,exposed/N,label='E',color='red')
        plt.plot(x_axis,exposed_q/N,label='Eq',color='black')
        plt.plot(x_axis,infected_u/N,label='Iu',color='brown')
        plt.plot(x_axis,infected_q/N,label='Iq',color='cyan')
        plt.plot(x_axis,infected_d/N,label='Id',color='orange')
        plt.plot(x_axis,death/N,label='D',color='purple')
        plt.plot(x_axis,recovered/N,label='R',color='magenta')
        plt.legend()
        plt.xlabel('Time (in days)')
        plt.ylabel('Fraction of population')
        plt.title('SARS Model with q value = ' + str(round(q,2)))
        plt.show()