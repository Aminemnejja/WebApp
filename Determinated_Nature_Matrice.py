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
    diagonales_nulles=diagonales_nulles_sup(matrice)
    if diagonales_nulles==0:
        return False,False
  
    return True,n-1-diagonales_nulles
def est_matrice_inf_bande(matrice):
    
    n = matrice.shape[0]
    
    # Vérifier si la matrice est une matrice triangulaire inférieure
    if not np.all(np.tril(matrice) == matrice):
        return False,False
    # Compter le nombre de diagonales non nulles
    diagonales_nulles =  diagonales_nulles_inf(matrice)
    if diagonales_nulles==0:
        return False,False




    return True,n-1-diagonales_nulles
def est_bande(matrice):
    matrice_inf = np.tril(matrice)
    matrice_sup = np.triu(matrice)
    a=est_matrice_inf_bande(matrice_inf)
    b=est_matrice_sup_bande(matrice_sup)
    if a[0] and b[0] :
        return True,max(a[1],b[1])
    else :
        return False,False
def message_info(matrix_type,A):
    if isinstance(matrix_type, str):
        return f"Type de matrice A détecté : {matrix_type}"
    elif matrix_type[0]=="matrice bande" and np.allclose(A, A.T): 
        return f"Type de matrice A détecté  est une matrice  bande symétrique  de largeur m=  {matrix_type[1]}"
    elif matrix_type[0]=="matrice bande" :
        return f"Type de matrice A détecté  est une matrice  bande   de largeur m=  {matrix_type[1]}"        
    else:
        
        return f"Type de matrice A détecté  est une matrice demi bande inférieur de largeur m=  {matrix_type[1]}"
def diagonales_nulles_sup(matrice):
    # Extraire les diagonales
    diagonales = [np.diag(matrice, k=-i) for i in range(-matrice.shape[0]+1, 0)]
    print(diagonales)
    # Compter les zéros dans chaque diagonale
    diagonales_nulles_count = 0
    for diag in diagonales:
        if np.all(diag==0):
            diagonales_nulles_count+=1
        else:
            break
            
    

    return diagonales_nulles_count
def diagonales_nulles_inf(matrice):
    # Extraire les diagonales
    diagonales = [np.diag(matrice, k=i) for i in range(-matrice.shape[0]+1, 0)]
    print(diagonales)
    # Compter les zéros dans chaque diagonale
    diagonales_nulles_count = 0
    for diag in diagonales:
        if np.all(diag==0):
            diagonales_nulles_count+=1
        else:
            break
            
    

    return diagonales_nulles_count