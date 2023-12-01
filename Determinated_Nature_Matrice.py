import numpy as np
# Fonction pour déterminer automatiquement le type de matrice
def determine_matrix_type(matrice,m=0):
    a=est_matrice_inf_bande(matrice)
    b=est_matrice_sup_bande(matrice)
    c=est_bande(matrice)
    if a[0]:
        return "demi bande inférieur",a[1]
    elif b[0]:
        return "demi bande supérieur" ,b[1]
    elif np.all(np.triu(matrice) == matrice):
        return "Triangulaire supérieure"
    elif np.all(np.tril(matrice) == matrice):
        return "Triangulaire inférieure"
    elif c[0]:
        return "matrice bande",c[1]
    elif np.array_equal(matrice, matrice.T):
        return "Symétrique"
    else:
        return "Dense"
def est_matrice_sup_bande(matrice):


    n = matrice.shape[0]
    if not np.all(np.triu(matrice) == matrice):
        return False,False

    # Compter le nombre de diagonales non nulles
    diagonales_non_nulles =  np.max(np.count_nonzero(np.triu(matrice,k=1), axis=1))
    if diagonales_non_nulles==n-1:
        return False,False
  

    # Parcourir chaque élément en dehors de la bande
    for i in range(n):
        for j in range(i,n):
            # Si l'élément est en dehors de la bande, il doit être égal à zéro
            if abs(i - j) > diagonales_non_nulles and matrice[i, j] != 0:
                
                return False,False
    m=diagonales_non_nulles
    return True,m
def est_matrice_inf_bande(matrice):
    
    n = matrice.shape[0]
    
    # Vérifier si la matrice est une matrice triangulaire inférieure
    if not np.all(np.tril(matrice) == matrice):
        return False,False
    # Compter le nombre de diagonales non nulles
    diagonales_non_nulles =  np.max(np.count_nonzero(np.tril(matrice,k=-1), axis=1))
    if diagonales_non_nulles==n-1:
        return False,False

  

    # Parcourir chaque élément en dehors de la bande
    for i in range(n):
        for j in range(i+1):
            # Si l'élément est en dehors de la bande, il doit être égal à zéro
            if abs(i - j) > diagonales_non_nulles and matrice[i, j] != 0:
                
                return False,False


    return True,diagonales_non_nulles
def est_bande(matrice):
    n=matrice.shape[0]
    matrice_inf=np.zeros((n,n))
    matrice_sup=np.zeros((n,n))
    for i in range(n):
        for j in range(i+1):
            matrice_inf[i,j]=matrice[i,j]
    for i in range(n):
         for j in range(i,n):
            matrice_sup[i,j]=matrice[i,j]
    a=est_matrice_inf_bande(matrice_inf)
    b=est_matrice_sup_bande(matrice_sup)
    if a[0] and b[0] and a[1]==b[1]:
        return True,a[1]
    else :
        return False,False
    
