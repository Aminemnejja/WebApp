import numpy as np

def multiplication_dense_dense(A,B,n):
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i, j] += A[i, k] * B[k, j]

    return result





def multiplication_matrice_band_demi_bande(A, B,m,n):
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(0,min(n,m+i+1)):
            for k in range(j,min(n,m+j+1)):
                result[i, j] += A[i, k] * B[k, j]

    return result





def multiplication_demi_bande_sup_bande(A, B,s,t,n):
    result = np.zeros((n, n))
    for i in range(n):
       
        for j in range(max(0,i-s),min(n,t+i+1)):


            for k in range(max(max(0,i-s),max(0,j-t)),min(i+1,j+1)):
                result[i, j] += A[i, k] * B[k, j]

    return result




def multiplication_bande_transposer(A,m,n):
    result = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(max(max(0,i-m),max(0,j-m)),min(min(n,m+i+1),min(n,m+j+1))):
                result[i, j] += A[i, k] * A[j,k]
                
    return result



def gauss_jordan_inverse(matrice, n):
    aug_matrix = np.hstack([matrice, np.eye(n)])
    
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
        for j in range(2 * n):
            aug_matrix[k, j] /= pivot
        
        # Éliminer les autres colonnes en dessous et au-dessus de la diagonale
        # Il faut i != k !!! Diviser en deux boucles
        for i in range(k):
                ratio = aug_matrix[i, k]
                for j in range(2 * n):
                    aug_matrix[i, j] -= ratio * aug_matrix[k, j]
        for i in range(k+1,n):
            ratio = aug_matrix[i, k]
            for j in range(2 * n):
                aug_matrix[i, j] -= ratio * aug_matrix[k, j]
            

    inverse_matrix = aug_matrix[:, n:]
    return inverse_matrix


def multiplication_bande_inverse(A,n,m):
    inverse_A=gauss_jordan_inverse(A, n)
    print(inverse_A)
    resultat = np.zeros((n, n))
    for i in range(n):
        for k in range(max(0,i-m),min(n,i+m+1)):
            resultat[i,i]+=A[i,k]*inverse_A[k,i]
    return resultat,inverse_A









