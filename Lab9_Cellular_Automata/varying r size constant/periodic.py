import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


#def check_corner(a,i,j):
#    if((i==0 and j==0) or (i==0 and j==len(a[0])-1) or (i==len(a)-1 and j==len(a[0])-1) or (i==len(a[0])-1 and j==0)):
#        return True
#    else:
#        return False
        
#def check_edge(a,i,j):  
#    if(i==0 or i==len(a)-1 or j==0 or j==len(a[0])-1):
#        return True
#    else:
#        return False


def attainedEQ(a,b,thresh):
    # equilibrium logic
    for i in range(len(a)):
        for j in range(len(a[0])):
            if abs(float(a[i][j]-b[i][j])) > thresh:
                #print(a[i][j]-b[i][j])
                return False
    return True

def sum_neighbour(a,i,j):
    cnt = 0
    #if(i-1 >= 0):
    cnt+= a[i-1][j]
    #if(i+1 < h):
    cnt+= a[i+1][j]
    #if(j-1 >= 0):
    cnt+= a[i][j-1]
    #if(j+1 < w):
    cnt+= a[i][j+1]
    #if(i-1 >= 0 and j-1 >= 0):
    cnt+= a[i-1][j-1]
    #if(i-1 >= 0 and j+1 < w):
    cnt+= a[i-1][j+1]
    #if(i+1 < h and j-1 >= 0):
    cnt+= a[i+1][j-1]
    #if(i+1 < h and j+1 < w):
    cnt+= a[i+1][j+1]
    return cnt
        
def update(data):
    mat.set_data(data)
    return mat 

def data_gen(a):
    cnt = 0
    eq = False
    h = len(a)
    w = len(a[0])
    while not eq: 

        if cnt < 10:
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

        b = np.zeros_like(a)
        b = np.copy(a)
        # operations on b
        for i in range(1,h-1):
            for j in range(1,w-1):
                b[i][j] = (1-8*r)*a[i][j] + r*sum_neighbour(a,i,j)
                #print(sum_neighbour(a,i,j))

        if ref_bound:
            for i in range(h):
                b[i][0] = b[i][1]
                b[i][h-1] = b[i][h-2]
            for i in range(w):
                b[0][i] = b[1][i]
                b[w-1][i] = b[w-2][i]
            b[0][0] = b[0][1]
            b[0][w-1] = b[0][w-2]
            b[h-1][0] = b[h-2][0]
            b[h-1][w-1] = b[h-2][w-2]
        if per_bound:
            for i in range(h):
                b[i][0] = b[i][h-2]
                b[i][h-1] = b[i][1]
            for i in range(w):
                b[0][i] = b[w-2][i]
                b[w-1][i] = b[1][i]
            b[0][0] = b[0][h-2]
            b[0][w-1] = b[0][1]
            b[h-1][0] = b[h-1][w-2]
            b[h-1][w-1] = b[h-1][1]

        cnt +=1
        #print(b-a)

        if attainedEQ(a,b,0.001):
            eq = True
            print('Equilibrium Attained at t = '+str(cnt))
            eq_array.append(cnt)
            #time[ii] = cnt
            #return cnt
        
        a = np.copy(b)
        yield a

R = [i/100 for i in range(5,13)]
#S = [15]
eq_array =[]
#time = np.zeros_like(size)
for ii in range(len(R)):
    r = R[ii]
    size = 10
    #size = size[ii]
    boundary = 1
    a = np.ones((size+boundary)*(size+boundary))*25
    a = a.reshape((size+boundary), (size+boundary))
    h= len(a)
    w= len(a[0])
    # ABSORBING BOUNDRY
    abs_bound = False
    ref_bound = False
    per_bound = True
    if abs_bound:
        for i in range((size+boundary)):
            a[i][0] = 25
            a[0][i] = 25
            a[i][size+boundary-1] = 25
            a[size+boundary-1][i] = 25
    if per_bound:
        for i in range(h):
            a[i][0] = a[i][h-2]
            a[i][h-1] = a[i][1]
        for i in range(w):
            a[0][i] = a[w-2][i]
            a[w-1][i] = a[1][i]
        a[0][0] = a[0][h-2]
        a[0][w-1] = a[0][1]
        a[h-1][0] = a[h-1][w-2]
        a[h-1][w-1] = a[h-1][1]
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
    #for i in range(1,h-1):
    #     a[i][1] = 50
    #     a[1][i] = 0

    #print(a)
    fig, ax = plt.subplots()
    mat = ax.matshow(a, cmap = 'magma')
    plt.colorbar(mat)
    ani = animation.FuncAnimation(fig, update, data_gen(a), interval=1000/1000,save_count=250)
    #writergif = animation.PillowWriter(fps=10)
    #ani.save(r'reflect.gif',writer=writergif)
    if abs_bound:
        plt.title('Absorbing Boundary')
    elif per_bound:
        plt.title('Periodic Boundary')
    elif ref_bound:
        plt.title('Reflective Boundary')
    plt.show()
#print(eq_array)
plt.figure(1)
plt.title("Time required to acheive equilibrium")
plt.plot(R,eq_array)
plt.grid()
plt.show()

