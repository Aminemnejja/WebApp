import numpy as np


def Gausse_soleide_converge(A, n):  
    E = np.zeros((n, n))
    D = np.zeros((n, n))
    F = np.zeros((n, n))

    for i in range(n):
        D[i][i] = A[i][i]
        for j in range(i):
            E[i][j] = -A[i][j]
        for j in range(i + 1, n):
            F[i][j] = -A[i][j]

    return check_convergence(np.dot(np.linalg.inv(D - E), F))

def Jacobie_converge(A, n):
    E = np.zeros((n, n))
    D = np.zeros((n, n))
    F = np.zeros((n, n))

    for i in range(n):
        D[i][i] = A[i][i]
        for j in range(i):
            E[i][j] = -A[i][j]
        for j in range(i + 1, n):
            F[i][j] = -A[i][j]

    return check_convergence(np.dot(np.linalg.inv(D), E + F))

def check_convergence(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    spectral_radius = max(abs(eigenvalues))
    if (spectral_radius < 1):
        return True
    else:
        return False


def jacobi_epsilon(A, B, n,eps):

    x = np.zeros(n)
    y = np.zeros(n)
    a= False
    while not a:
   
        x = np.copy(y)

        for i in range(n):
            s = B[i]
            for j in range(n):
                if j == i:
                    continue
                s -= A[i, j] * x[j]
            y[i] = s / A[i, i]
        if np.max(np.abs(x- y)) < eps:
            a = True
  
    return x
def Gauss_Seidel_epsilon(A, B, n, eps):
    x = np.zeros(n)

    max_diff = float('inf')  # Initialiser à l'infini pour entrer dans la boucle

    while max_diff > eps:
  
        max_diff = 0

        for i in range(n):
            s = 0
            for j in range(n):
                if i == j:
                    continue
                s += A[i, j] * x[j]
            
            prev_x_i = x[i]
            x[i] = (B[i] - s) / A[i, i]

            # Mettre à jour la différence maximale
            max_diff = max(max_diff, np.abs(prev_x_i - x[i]))
            

    return x
def jacobi_fixed_iterations(A, B, n, num_iterations):
    x = np.zeros(n)
    y = np.zeros(n)

    for _ in range(num_iterations):
        x = np.copy(y)

        for i in range(n):
            s = B[i]
            for j in range(n):
                if j == i:
                    continue
                s -= A[i, j] * x[j]
            y[i] = s / A[i, i]

    return x

def Gauss_Seidel_fixed_iterations(A, B, n, num_iterations):
    x = np.zeros(n)

    for _ in range(num_iterations):
        for i in range(n):
            s = 0
            for j in range(n):
                if i == j:
                    continue
                s += A[i, j] * x[j]
            x[i] = (B[i] - s) / A[i, i]

    return x


A = np.array([[2, 1],
             [5, 3]])
B = np.array([1, 0])
n = A.shape[0]
eps = 1e-10
num_iterations=1000
result_jacobi = jacobi_epsilon(A, B, n, eps)
result_soleide=Gauss_Seidel_epsilon(A, B, n, eps)
print(jacobi_fixed_iterations(A, B, n, num_iterations))
print(Gauss_Seidel_fixed_iterations(A, B, n, num_iterations))

print("Solution Jacobi:", result_jacobi)
print("solution ",result_soleide)
