import os
import numpy as np
from matplotlib import pyplot as plt
import numpy
import scipy
import pandas as pd
import random

# position v/s time with varying runs
# unbiased
runs = [10, 100,1000]
seed = 22
steps = 50
random.seed(seed)
count=0
color=["#fc5185","#3fc1c9","#364f6b"]
for r in runs:
    net_pos_x = []
    net_pos_y = []
    dist = []
    for i in range(1,r):
        posX = np.zeros(steps)
        posY = np.zeros(steps)
        for j in range(len(posX)):
            val = np.random.uniform(0,1)
            if(val<0.19):#N
                posX[j] = posX[j-1] + 0
                posY[j] = posY[j-1] + 1
            elif(val<0.43):#NE
            
                posX[j] = posX[j-1] + 1/np.sqrt(2)
                posY[j] = posY[j-1] + 1/np.sqrt(2)
        
            elif(val<0.6):#E
            
                posX[j] = posX[j-1] + 1
                posY[j] = posY[j-1] + 0
            
            elif(val<0.7):#sE
            
                posX[j] = posX[j-1] + 1/np.sqrt(2)
                posY[j] = posY[j-1] - 1/np.sqrt(2)
            
            elif(val<0.72):#S
            
                posX[j] = posX[j-1] + 0
                posY[j] = posY[j-1] - 1
            
            elif(val<0.75):#SW
            
                posX[j] = posX[j-1] - 1/np.sqrt(2)
                posY[j] = posY[j-1] - 1/np.sqrt(2)
            
            elif(val<0.85):#W
            
                posX[j] = posX[j-1] - 1
                posY[j] = posY[j-1] + 0
            
            else: #NW
            
                posX[j] = posX[j-1] - 1/np.sqrt(2)
                posY[j] = posY[j-1] + 1/np.sqrt(2)
            
            
        net_pos_x.append(posX)
        net_pos_y.append(posY)
    
    net_pos_x = np.array(net_pos_x)
    net_pos_y = np.array(net_pos_y)
    posX = []
    posY = []

    # pos = pos/r
    for i in range(steps):
        posX.append(np.average(net_pos_x[:,i]))
        posY.append(np.average(net_pos_y[:,i]))
        dist.append(np.sqrt(posX[i]**2 + posY[i]**2)) 
        
    plt.grid(b = True, color ='grey',  linestyle ='-.', linewidth = 0.5, alpha = 0.6)
    plt.xlabel('No of steps')
    plt.ylabel('Average distance from origin')
    #plt.plot(posX,posY,color=color[count])
    plt.plot(dist,color=color[count])
    plt.title('Unbiased walk for ')
    count = count+1
    # plt.title('Unbiased walk for ' + str(r) + " runs")
#x = np.linspace(-50,50,1000)
#y = np.sqrt(2500 - x*x)
#y1 = -1*y
#y = y.tolist()
#y1 = y1.tolist()
#y.pop(int(len(y)/2))
#y.append(y1)
# for i in range(len(x)):
#     x[i] = steps * np.cos(theta[i])
#     y[i] = steps * np.sin(theta[i])
#plt.plot(x,y, linewidth = 1)
plt.legend(['100 runs','1000 runs','10000 runs','circle'])
plt.show()
