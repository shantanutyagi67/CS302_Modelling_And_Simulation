import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation




# 0 - Empty
# 1 - tree
# 2 - burning

def spread(a,c,i,j,h,w):
    if(a[i][j]==0):
        return 0,c
    if(c[i][j]==1):
        c[i][j]=0
        return 0,c
    if(a[i][j]==1):
        cnt=0
        temp = np.random.uniform(0,1)
        if(temp<prob_immune):
            return 1,c
        temp = np.random.uniform(0,1)
        if(temp<prob_lightning):
            return 2,c
            
        if(i-1 >= 0 and a[i-1][j]==2 ):
            cnt+=1 
        if(i+1 < h and a[i+1][j]==2 ):
            cnt+=1 
        if(j-1 >= 0 and a[i][j-1]==2):
            cnt+=1 
        if(j+1 < w and a[i][j+1]):
            cnt+=1
        if(cnt>=2):
            return 2,c
        if(cnt<2):
            return 1,c

    if(a[i][j]==2):
        c[i][j]=1
        return 1,c
        
def update(data):
    mat.set_data(data)
    return mat 

def data_gen(a):
    cnt = 0
    eq = False
    h = len(a)
    w = len(a[0])
    c=np.zeros_like(a)
    while cnt<100:
        print(cnt)
        
        b = np.copy(a)

        
        # operations on b
        for i in range(1,h-1):
            for j in range(1,w-1):
                b[i][j],_ = spread(a,c,i,j,h,w)
        
        cnt +=1
        for i in range(h):
            b[i][0] = b[i][h-2]
            b[i][h-1] = b[i][1]
        for i in range(w):
            b[0][i] = b[w-2][i]
            b[w-1][i] = b[1][i]

        a = np.copy(b)
        yield a

#S = [8,10,12,14,16,18,20,22,24,26,28,30]
# 0 - Empty
# 1 - tree
# 2 - burning
S = [50]
eq_array =[]
prob_tree = 0.75
prob_burning = 0.05
prob_immune = 0.25
prob_lightning = 0.001
boundary = 1
for ii in S:
    a = np.zeros((ii+boundary)*(ii+boundary))
    a = a.reshape(ii+boundary, ii+boundary)
    h= len(a)
    w= len(a[0])
    size = ii+boundary
    for i in range(1,size-1):
        for j in range(1,size-1):    
            temp = np.random.uniform(0,1)
            if(temp<prob_tree):
                temp2 = np.random.uniform(0,1)
                if(temp2<prob_burning):
                    a[i][j] = 2
                else:
                    a[i][j] = 1
    for i in range(h):
            a[i][0] = a[i][h-2]
            a[i][h-1] = a[i][1]
    for i in range(w):
        a[0][i] = a[w-2][i]
        a[w-1][i] = a[1][i]
    # initialization done
    
    c=plt.imshow(a,cmap="viridis",interpolation ='nearest', origin ='lower')
    plt.colorbar(c)
    plt.show() 
    fig, ax = plt.subplots()
    mat = ax.matshow(a, cmap = 'magma')
    plt.colorbar(mat)
    ani = animation.FuncAnimation(fig, update, data_gen(a), interval=1000/1000,save_count=100)
    writergif = animation.PillowWriter(fps=10)
    ani.save(r'1.gif',writer=writergif)
    plt.show()
    

