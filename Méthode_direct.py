import numpy as np
import Systeme_Lineaire_Triangulaire as t



def gauss_jordan_dense(matrice ,b,n):
    aug_matrix = np.hstack([matrice, b])

    for k in range(n):
        # Trouver l'indice de la ligne avec le pivot maximal
        max_pivot_index = np.argmax(np.abs(aug_matrix[k:, k])) + k
        
        # Échanger les lignes si le pivot est nul
        if aug_matrix[max_pivot_index, k] == 0:
            # Gestion du cas où toutes les entrées sous la colonne k sont nulles
            continue
        else:
            aug_matrix[[k, max_pivot_index], :] = aug_matrix[[max_pivot_index, k], :]

        # Échelonner la colonne k
        pivot = aug_matrix[k, k]

        # Diviser chaque élément de la ligne par le pivot
        for j in range(k+1,n+1):
            aug_matrix[k, j] /= pivot
        
        # Éliminer les autres colonnes en dessous et au-dessus de la diagonale
        # Il faut i != k !!! Diviser en deux boucles
        for i in range(k):
                ratio = aug_matrix[i, k]
                for j in range(k+1,n+1):
                    aug_matrix[i, j] -= ratio * aug_matrix[k, j]
        for i in range(k+1,n):
            ratio = aug_matrix[i, k]
            for j in range(k+1,n+1):
                aug_matrix[i, j] -= ratio * aug_matrix[k, j]
                
    return aug_matrix[:n,n]
       
def gauss_jordan_dense_symetrique(matrice, b,n):
    aug_matrix = np.hstack([matrice, b])
    
    for k in range(n):
        # Ã‰chelonner la colonne k
        pivot = aug_matrix[k, k]
        # Diviser chaque Ã©lÃ©ment de la ligne par le pivot
        for j in range(k+1,n+1):
            aug_matrix[k, j] /= pivot
        
        # Ã‰liminer les autres colonnes en dessous et au-dessus de la diagonale
        # Il faut i != k !!! Diviser en deux boucles
        for i in range(k):
                ratio = aug_matrix[i, k]
                for j in range(k+1,n+1):
                    
                    aug_matrix[i, j] -= ratio * aug_matrix[k, j]
    
        for i in range(k+1,n):
            ratio = aug_matrix[i, k]
            for j in range(i,n):#travailler sur partie supÃ©rieur car matrice symÃ©trique
                
                aug_matrix[i, j] -= ratio * aug_matrix[k, j]
                aug_matrix[j,i]=aug_matrix[i,j]
            #Traitement pour vecteur b
            aug_matrix[i, n] -= ratio * aug_matrix[k, n]

            
     

    return aug_matrix[:n,n]
def gauss_jordan_bande_symetrique(matrice, b,n,m):
    aug_matrix = np.hstack([matrice, b])
    
    for k in range(n):
     
        # Ã‰chelonner la colonne k
        pivot = aug_matrix[k, k]
        # Diviser chaque Ã©lÃ©ment de la ligne par le pivot
        for j in range(k+1,n+1):
            aug_matrix[k, j] /= pivot
        
        # Ã‰liminer les autres colonnes en dessous et au-dessus de la diagonale
        # Il faut i != k !!! Diviser en deux boucles
        for i in range(k):
            
                ratio = aug_matrix[i, k]
             
                for j in range(k+1,n+1):
                    
                    aug_matrix[i, j] -= ratio * aug_matrix[k, j]
    
        for i in range(k+1,min(n,k+m+1)):
          
            ratio = aug_matrix[i, k]
            for j in range(i,n):#travailler sur partie supÃ©rieur car matrice symÃ©trique
                
                aug_matrix[i, j] -= ratio * aug_matrix[k, j]
                aug_matrix[j,i]=aug_matrix[i,j]
            #Traitement pour vecteur b
            aug_matrix[i, n] -= ratio * aug_matrix[k, n]

        
        
    return aug_matrix[:n,n]


def elimination_gaussienne_sans_pivot_dense_symetrique(A, b,n):
    for k in range(n-1):
        for i in range(k+1, n):
            factor = A[k][i] / A[k][k]
            for j in range(i, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
    
    return  t.sys_lin_sup_dense(A, b, n)



def elimination_gaussienne_sans_pivot_bande_symetrique(A, b, n,m):
    for k in range(n):
        for i in range(k+1,min(k+m+1,n)):
            factor = A[k][i] / A[k] [k]
            for j in range(i,min(k+m+1,n)):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
    return t.sys_lin_sup_demiBande(A, b, n, m)
def decomposition_LU_dense(A,n):
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    for k in range(n):
        L[k][k] = 1
        for j in range(k, n):
            U[k][j] = A[k][j] - sum(L[k][i] * U[i][j] for i in range(k))
            
        for i in range(k + 1, n):
            L[i, k] = (A[i][k] - sum(L[i][j] * U[j][k] for j in range(k))) / U[k][k]
    return L,U
def decomposition_LU_bande(A,n,m):

    L = np.zeros((n, n))  
    U = np.zeros((n, n))

    for k in range(n):
        L[k][k] = 1 

        for j in range(max(0, k - m), n):
            U[k][j] = A[k][j] - sum(L[k][i] * U[i][j] for i in range(k))
        for i in range(k + 1, n):
            L[i][k] = (A[i][k] - sum(L[i][j] * U[j][k] for j in range(k))) / U[k][k]
    return L,U
def decomposition_LU_Dense_Symetrique(A,n):
    #pour matrice symétrique A=L*D*Transposée(L)

    L = np.zeros_like(A, dtype=float)
    D = np.zeros(n, dtype=float)

    for i in range(n):
        for j in range(i+1):
                s = A[i, j]
                for k in range(j):
                    s -= L[i, k]**2 * D[k]
                D[i] = s
                s = A[i, j]
                for k in range(j):
                    s -= L[i, k] * L[j, k] * D[k]
                L[i, j] = s / D[j]


    return L, np.diag(D)
def decomposition_LU_bande_Symetrique(A, n,m):
    #pour matrice symétrique A=L*D*Transposée(L)
    L = np.zeros_like(A, dtype=float)
    D = np.zeros(n, dtype=float)

    for i in range(n):
        L[i,i]=1
        for j in range(max(0, i - m), i + 1):
            s = A[i, j]
            for k in range(max(j - m, 0), j):
                s -= L[i, k] * L[j, k] * D[k]
            if i == j:
                D[i] = s
            else:
                L[i, j] = s / D[j]

    return L, np.diag(D)
def decomposition_cholesky_dense(A,n):
    L = np.zeros((n, n))

    for j in range(n):
        L[j][j]=A[j][j]
        for k in range(j):
            L[j][j] -= L[j][k]*L[j][k]
        L[j][j]=np.sqrt(L[j][j])
        for i in range(j+1,n):
            L[i][j] = A[i][j]
            for k in range(j):
                L[i][j] -= L[i][k]*L[j][k]
            L[i][j]/=L[j][j]
    return L

def decomposition_cholesky_bande(A,n,m):

    L = np.zeros((n, n))
    for j in range(n):
        L[j][j] = A[j][j]
        for k in range(j):
            L[j][j] -= L[j][k]*L[j][k]
        L[j][j]=np.sqrt(L[j][j])
        for i in range(j+1,min(j+m+1,n)):
            L[i][j] = A[i][j]
            for k in range(j):
                L[i][j] -= L[i][k]*L[j][k]
            L[i][j]/=L[j][j]
    return L
            


def elimination_gaussienne_avec_pivot_dense(A,b,n):
 
    
    for k in range(n-1):
        # Trouver l'indice de la ligne avec le pivot maximal
        max_pivot_index = np.argmax(np.abs(A[k:, k])) + k
        # Échanger les lignes si le pivot est nul
        if A[max_pivot_index, k] == 0:
            continue
        else:
            A[[k, max_pivot_index],:] = A[[max_pivot_index, k], :]
            b[[k, max_pivot_index]] = b[[max_pivot_index, k]]

        # Échelonner la colonne k
        pivot = A[k][k]
        for i in range(k+1, n):
            A[i][k] /= pivot 
            for j in range(k+1, n):
                A[i][j] -= A[i][k]* A[k][j]
            b[i] -= A[i][k] * b[k] 
    return t.sys_lin_sup_dense(A, b, n)


def elimination_gaussienne_avec_pivot_bande(A, b, n,m):
    xn=2*m+1
    for k in range(n-1):
        # Trouver l'indice de la ligne avec le pivot maximal
        max_index = np.argmax(np.abs(A[k:, k])) + k +1

        # Échanger les lignes si le pivot est nul
        if A[max_index - 1, k] == 0:
            continue
        else:
            A[[k, max_index - 1], :] = A[[max_index - 1, k], :]
            b[[k, max_index - 1]] = b[[max_index - 1, k]]

        # Échelonner la colonne k
        pivot = A[k][k]
        for i in range(k + 1, min(k + xn + 1, n)):
            A[i][k] /= pivot
            for j in range(k + 1, min(k + xn + 1, n)):
                A[i][j] -= A[i][k] * A[k][j]
            b[i] -= A[i][k] * b[k]
        

    return t.sys_lin_sup_dense(A, b, n)


