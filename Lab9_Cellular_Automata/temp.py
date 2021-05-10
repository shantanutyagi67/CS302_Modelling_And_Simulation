import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation







# def attainedEQ(a,b,thresh):
#     # equilibrium logic
#     # print(a-b)
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             if abs(float(a[i][j]-b[i][j])) > thresh:
#                 #print(a[i][j]-b[i][j])
#                 return False
#     return True
    

# def sum_neighbour(a,i,j):
#     cnt = 0
#     #if(i-1 >= 0):
#     cnt+= a[i-1][j]
#     #if(i+1 < h):
#     cnt+= a[i+1][j]
#     #if(j-1 >= 0):
#     cnt+= a[i][j-1]
#     #if(j+1 < w):
#     cnt+= a[i][j+1]
#     #if(i-1 >= 0 and j-1 >= 0):
#     cnt+= a[i-1][j-1]
#     #if(i-1 >= 0 and j+1 < w):
#     cnt+= a[i-1][j+1]
#     #if(i+1 < h and j-1 >= 0):
#     cnt+= a[i+1][j-1]
#     #if(i+1 < h and j+1 < w):
#     cnt+= a[i+1][j+1]
#     return cnt
        

# def data_gen(a):
#     cnt = 0
#     h= len(a)
#     w= len(a[0])
#     eq = False
#     #while not eq: 

#     a[1][1] = 100
#     a[1][2] = 100
#     a[2][1] = 100
#     a[1][3] = 100
#     a[3][1] = 100
#     a[2][2] = 100
#     a[3][3] = 100
#     h-=1
#     a[h-1][h-1] = 0
#     a[h-1][h-2] = 0
#     a[h-2][h-1] = 0
#     a[h-1][h-3] = 0
#     a[h-3][h-1] = 0
#     a[h-2][h-2] = 0
#     a[h-3][h-3] = 0
#     h+=1
#     #print(b.shape)
#     #b = a
#     #print(b.dtype)
#     # operations on b
#     for i in range(1,h-1):
#         for j in range(1,w-1):
#             b[i][j] = float((1-8*r)*a[i][j] + r*sum_neighbour(a,i,j))
#             #print(b[i][j] - a[i][j])
#             #print(sum_neighbour(a,i,j))

#     #if np.array_equal(a,b):
#     #    print("HOW?")

#     if ref_bound:
#         for i in range(h):
#             b[i][0] = b[i][1]
#             b[i][h-1] = b[i][h-2]
#         for i in range(w):
#             b[0][i] = b[1][i]
#             b[w-1][i] = b[w-2][i]
#         b[0][0] = b[0][1]
#         b[0][w-1] = b[0][w-2]
#         b[h-1][0] = b[h-2][0]
#         b[h-1][w-1] = b[h-2][w-2]
#     if per_bound:
#         for i in range(h):
#             b[i][0] = b[i][2]
#             b[i][h-1] = b[i][h-3]
#         for i in range(w):
#             b[0][i] = b[2][i]
#             b[w-1][i] = b[w-3][i]
#         b[0][0] = b[2][2]
#         b[0][w-1] = b[2][w-3]
#         b[h-1][0] = b[h-3][2]
#         b[h-1][w-1] = b[h-3][w-3]

#     cnt +=1
#     #print(cnt)
#     #print(a)
#     #print(b)
#     #print(a-b)
#     if ((attainedEQ(a,b,0.001)) and (cnt!=1)):
#         eq = True 
#         #print(attainedEQ(a,b,0.001))
#         print('Equilibrium Attained at t = '+str(cnt))
        
#         #time[ii] = cnt
#         #return cnt
    
#     return b

#S = [8,10,12,14,16,18,20,22,24,26,28,30]
S = [15]
eq_array =[]
#time = np.zeros_like(size)
for ii in range(len(S)):
    r = 0.1
    size = S[ii]
    #size = size[ii]
    boundary = 1
    a = np.ones((size+boundary)*(size+boundary))*25
    a = a.reshape((size+boundary), (size+boundary))
    b = np.zeros_like(a)
    h= len(a)
    w= len(a[0])
    print(a.dtype)
    # ABSORBING BOUNDRY
    abs_bound = True
    ref_bound = False
    per_bound = False
    if abs_bound:
        for i in range((size+boundary)):
            a[i][0] = 25
            a[0][i] = 25
            a[i][size+boundary-1] = 25
            a[size+boundary-1][i] = 25
    if per_bound:
        for i in range(h):
            a[i][0] = a[i][2]
            a[i][h-1] = a[i][h-3]
        for i in range(w):
            a[0][i] = a[2][i]
            a[w-1][i] = a[w-3][i]
        a[0][0] = a[2][2]
        a[0][w-1] = a[2][w-3]
        a[h-1][0] = a[h-3][2]
        a[h-1][w-1] = a[h-3][w-3]
    if ref_bound:
        for i in range(h):
            a[i][0] = a[i][1]
            a[i][h-1] = a[i][h-2]
        for i in range(w):
            a[0][i] = a[1][i]
            a[w-1][i] = a[w-2][i]
        a[0][0] = a[0][1]
        a[0][w-1] = a[0][w-2]
        a[h-1][0] = a[h-2][0]
        a[h-1][w-1] = a[h-2][w-2]

    a[1][1] = 100
    a[1][2] = 100
    a[2][1] = 100
    a[1][3] = 100
    a[3][1] = 100
    a[2][2] = 100
    a[3][3] = 100
    h-=1
    a[h-1][h-1] = 0
    a[h-1][h-2] = 0
    a[h-2][h-1] = 0
    a[h-1][h-3] = 0
    a[h-3][h-1] = 0
    a[h-2][h-2] = 0
    a[h-3][h-3] = 0
    h+=1
    for j in range(100):
        a = data_gen(a)
        print(j)