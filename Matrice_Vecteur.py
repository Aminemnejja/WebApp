import numpy as np

def Matrice_Dense(A, b, n):
    y = np.zeros(n)
    for i in range(n):
        for j in range(n):
            y[i] += A[i, j] * b[j]
    return y


def Matrice_inf(A, b, n):
    y = np.zeros(n)
    for i in range(n):
        for j in range(i+1):
            y[i] += A[i, j] * b[j]
    return y


def Matrice_sup(A, b, n):
    y = np.zeros(n)
    for i in range(n):
        for j in range(i, n):
            y[i] += A[i, j] * b[j]
    return y


def Matrice_demi_bande_inf(A, b, n, m):
    y = np.zeros(n)
    for i in range(n):
        print(i)
        for j in range(max(0, i-m), i+1):
            y[i] += A[i, j] * b[j]
    return y
def Matrice_demi_bande_sup(A,b,n,m):
    y = np.zeros(n)
    for i in range(n):
        for j in range (i,max(n, i-m)):
            y[i] += A[i, j] * b[j]
    return y
