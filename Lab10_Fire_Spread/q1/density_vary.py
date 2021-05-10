import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation



def density(a,h,w):
    cnt = 0
    for i in range(1,h-1):
        for j in range(1,w-1):
            if(a[i][j]==1):
                cnt+=1
    cnt = cnt/((h-1)*(w-1))
    return cnt

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
        if(cnt>=1):
            return 2,c
        if(cnt<1):
            return 1,c

    if(a[i][j]==2):
        c[i][j]=1
        return 1,c

def data_gen(a):
    cnt = 0
    eq = False
    h = len(a)
    w = len(a[0])
    c=np.zeros_like(a)
    while cnt<100:
        b = np.zeros_like(a)
        b = np.copy(a)

        # operations on b
        for i in range(1,h-1):
            for j in range(1,w-1):
                b[i][j],c = spread(a,c,i,j,h,w)
        
        cnt +=1
        for i in range(h):
            b[i][0] = b[i][h-2]
            b[i][h-1] = b[i][1]
        for i in range(w):
            b[0][i] = b[w-2][i]
            b[w-1][i] = b[1][i]

        a = np.copy(b)
    return density(a,h,w)

final_density = []
final_density_actual = []
den = np.linspace(0,1,11)
S = 50
eq_array =[]
# prob_burning_array = [0.005 , 0.05, 0.5]
# prob_burning = 0.005
prob_burning_array = np.linspace(0,1,11)
prob_immune = 0
prob_lightning = 0
boundary = 1
runs = 10
plot_1 = []
plot_2 = []

for prob_burning in prob_burning_array:
    final_density = []
    final_density_actual = []

    for jj in range(len(den)):
        prob_tree = den[jj]
        ans =0
        print(prob_tree)
        for kk in range(runs):
            
            # for ii in S:
                
            a = np.zeros((S+boundary)*(S+boundary))
            a = a.reshape(S+boundary, S+boundary)
            h= len(a)
            w= len(a[0])
            size = S+boundary
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
        ans += data_gen(a)

        if prob_tree==0:
            final_density.append(1)
            final_density_actual.append(0)
        else:    
            final_density.append(ans/(runs*prob_tree))
            final_density_actual.append(ans/runs)
    plot_1.append(final_density)
    plot_2.append(final_density_actual)

plt.figure(1)
for i in range(len(prob_burning_array)):
    plt.plot(den,plot_1[i],label="prob_burning  = "+str(i/10))
plt.grid()
plt.xlabel("Initial forest density")
plt.ylabel("Proportion of forest cover left with repsect to initial cover")
plt.title("Proportional Forest density")
plt.legend()
plt.show()

plt.figure(2)
for i in range(len(prob_burning_array)):
    plt.plot(den,plot_2[i],label="prob_burning  = "+str((i/10)))
plt.grid()
plt.xlabel("Initial forest density")
plt.ylabel("Final forest cover left ")
plt.title("Forest density")
plt.legend()
plt.show()
