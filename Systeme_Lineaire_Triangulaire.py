import numpy as np
def sys_lin_inf_dense(a,b,n):
   

    x=np.zeros(n)
    for i in range(n):
        x[i]=b[i]
        for j in range(i):
            x[i]-=a[i][j]*x[j]
        x[i]=x[i]/a[i][i]  
    return x


def sys_lin_sup_dense(a,b,n):
   
 
    x=np.zeros(n)
    for i in range(n-1,-1,-1):
        x[i]=b[i]
        for j in range(i+1,n):
            x[i]-=a[i][j]*x[j]
        x[i]=x[i]/a[i][i]  
    return x


def sys_lin_inf_demiBande(a, b, n,m):

    x = np.zeros(n)
    for i in range(n):
        x[i] = b[i]
        for j in range(max(0, i - m ), i):
            x[i] -= a[i][j] * x[j]
        x[i] = x[i] / a[i][i]  
    return x




def sys_lin_sup_demiBande(a, b, n,m):
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        x[i] = b[i]
        for j in range(i+1,min(i+m+1,n)):
            x[i] -= a[i][j] * x[j]
        x[i] = x[i] / a[i][i]  
    return x






