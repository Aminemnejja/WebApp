import streamlit as st
import numpy as np
import Determinated_Nature_Matrice as dt
import FLASK as f
import Systeme_Lineaire_Triangulaire as t
import Méthode_direct as m
import Méthode_itérative as I
import Fraction as FR 

def est_decomposable_LU(matrice):
    n = matrice.shape[0]

    for k in range(n):
        mineur_principal = matrice[:k+1, :k+1]
        print(mineur_principal)
        determinant_mineur = np.linalg.det(mineur_principal)

        if determinant_mineur == 0:
            return False  # Un mineur principal est nul, donc la matrice n'est pas décomposable sur LU

    return True  # Tous les mineurs principaux sont non nuls, la matrice est décomposable sur LU


def main():

    st.header(" Résolution de systéme : Ax=b")
    selected_option = st.radio("Sélectionnez une méthode", ["Méthode direct" ,"Méthode itérative" ])
    matrice_html=f.matriceA_html()
    vecteur_html=f.vecteur_html()
    col1, col2 = st.columns([3,1])
    with col1:
        st.components.v1.html(matrice_html,width=600, height=600)
    with col2:
        st.components.v1.html(vecteur_html,width=300, height=600)
    if selected_option=="Méthode direct":
        operation = st.selectbox("Choisissez l'opération ", ["Gauss","Gauss_jordan","Décomposition LU","Cholesky"])
         
        if st.button("Résoudre"):
            try:
                A=np.array(f.get_matrix_values_A(),dtype=float)
                n=A.shape[0]
                b=np.array(f.get_vector_values(),dtype=float)
                if n!=np.size(b):
                    st.warning("Les dimensions de matrice A et vecteur B doit etre égale")
                    exit(0)
                if np.linalg.det(A) == 0:
                    if np.linalg.norm(b) == 0:
                      st.warning("Infiniment de solutions ")
                      exit(0)
                    else:
                      st.warning("Aucune solution ")
                      exit(0)
                else :
                    rang_A = np.linalg.matrix_rank(A)
     
                    if rang_A != A.shape[1]:
                        st.warning("Infiniment de solutions ")
                        exit(0)
                
                matrix_type_A = dt.determine_matrix_type(A)
                st.success(dt.message_info(matrix_type_A, A))
    
                if operation=="Gauss":
                    if matrix_type_A[0]=="matrice bande" and np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) > 0) :
                        x=m.elimination_gaussienne_sans_pivot_bande_symetrique(A, b,n, matrix_type_A[1])
                        
                        st.dataframe(FR.matrix_to_fraction(x))
                        
                    elif matrix_type_A=="Symétrique" and np.all(np.linalg.eigvals(A) > 0):
                        x=m.elimination_gaussienne_sans_pivot_dense_symetrique(A, b, n)
                        
                        st.dataframe(FR.matrix_to_fraction(x))
                    elif matrix_type_A=="matrice bande":
                        x=m.elimination_gaussienne_avec_pivot_bande(A, b, n, m)
                        st.dataframe(FR.matrix_to_fraction(x))
                    else:
                        x=m.elimination_gaussienne_avec_pivot_dense(A, b, n)
                        st.dataframe(FR.matrix_to_fraction(x))
                elif operation=="Gauss_jordan":
                    b = b[:, np.newaxis]
                    if matrix_type_A[0]=="matrice bande" and np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) > 0) :
                        x=m.gauss_jordan_bande_symetrique(A, b, n, matrix_type_A[1])
                        st.dataframe(FR.matrix_to_fraction(x))
                    elif matrix_type_A=="Symétrique" and np.all(np.linalg.eigvals(A) > 0):
                        x=m.gauss_jordan_dense_symetrique(A, b, n)
                        st.dataframe(FR.matrix_to_fraction(x))
                    else:
                        x=m.gauss_jordan_dense(A, b, n)
                        st.dataframe(FR.matrix_to_fraction(x))
                elif operation=="Décomposition LU":
                  
                    if  matrix_type_A[0]=="matrice bande" and np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) >0):
                        st.header("A=L.D.L\u1D57")
                        L,D=m.decomposition_LU_bande_Symetrique(A, n, matrix_type_A[1])
                        U=np.dot(D,L.T)
                        y = t.sys_lin_inf_demiBande(L, b,n, matrix_type_A[1])
                        x = t.sys_lin_sup_demiBande(U, y,n, matrix_type_A[1])
                        col1,col2=st.columns(2)
                        with col1:
                                
                                st.dataframe(FR.matrix_to_fraction(L))
                        with col2:
                                
                                st.dataframe(FR.matrix_to_fraction(U))
                        st.write("X=")
                        st.dataframe(FR.matrix_to_fraction(x))
                        
                    elif matrix_type_A[0]=="matrice bande"  and  est_decomposable_LU(A) :
                        st.header("A=L.D")
                        L,U=m.decomposition_LU_bande(A, n, matrix_type_A[1])
                        y = t.sys_lin_inf_demiBande(L, b,n, matrix_type_A[1])
                        x = t.sys_lin_sup_demiBande(U, y,n, matrix_type_A[1])
                        col1,col2=st.columns(2)
                        with col1:
                                
                                st.dataframe(FR.matrix_to_fraction(L))
                        with col2:
                                
                                st.dataframe(FR.matrix_to_fraction(U))
                        st.write("X=")
                        st.dataframe(FR.matrix_to_fraction(x))
                    elif  matrix_type_A[0]=="Symétrique" and np.all(np.linalg.eigvals(A) >0):
                        st.header("A=L.D.L\u1D57")
                        L,D=m.decomposition_LU_dense_Symetrique(A, n)
                        U=np.dot(D,L.T)
                        y = t.sys_lin_inf_dense(L, b,n)
                        x = t.sys_lin_sup_dense(U, y,n)
                        col1,col2=st.columns(2)
                        with col1:
                                
                                st.dataframe(FR.matrix_to_fraction(L))
                        with col2:
                                
                                st.dataframe(FR.matrix_to_fraction(U))
                        st.write("X=")
                        st.dataframe(FR.matrix_to_fraction(x))
                    elif  est_decomposable_LU(A) :
                        st.header("A=L.D")
                        L,U=m.decomposition_LU_dense(A, n)
                        y = t.sys_lin_inf_dense(L, b,n)
                        x = t.sys_lin_sup_dense(U, y,n)
                        col1,col2=st.columns(2)
                        with col1:
                                
                                st.dataframe(FR.matrix_to_fraction(L))
                        with col2:
                                
                                st.dataframe(FR.matrix_to_fraction(U))
                        st.write("X=")
                        st.dataframe(FR.matrix_to_fraction(x))
                    else :
                        st.error("Matrice n'est pas décompasable")
                
                elif operation=="Cholesky":
                    st.header("A=L.L\u1D57")
                    if matrix_type_A[0]=="matrice bande"  and np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) > 0) :
                        L=m.decomposition_cholesky_bande(A, n, matrix_type_A[1])
                        LT=L.T
                        y = t.sys_lin_inf_demiBande(L, b, n, matrix_type_A[1])
                        x = t.sys_lin_sup_demiBande(LT, y, n, matrix_type_A[1])
                        col1,col2=st.columns(2)
                        with col1:
                            
                            st.dataframe(FR.matrix_to_fraction(L))
                        with col2:
                            
                            st.dataframe(FR.matrix_to_fraction(LT))
                        st.write("X=")
                        st.dataframe(FR.matrix_to_fraction(x))
                        
                    elif matrix_type_A=="Symétrique"  and np.all(np.linalg.eigvals(A) > 0) :
                        L=m.decomposition_cholesky_dense(A, n)
                        LT=L.T
                        y = t.sys_lin_inf_dense(L, b, n)
                        x = t.sys_lin_sup_dense(LT, y, n)
                        col1,col2=st.columns(2)
                        with col1:
                           
                            st.dataframe(FR.matrix_to_fraction(L))
                        with col2:
                           
                            st.dataframe(FR.matrix_to_fraction(LT))
                        st.write("X=")
                        st.dataframe(FR.matrix_to_fraction(x))
                    else:
                        st.error("Matrice doit etre symétrique et definie positive")
            except ValueError as e:
                     st.error(f"Erreur lors de la conversion des données de la matrice A ou B : {str(e)}")
            except Exception as ex:
                     st.error(f"Une exception s'est produite lors de la résolution  de systéme  : {str(ex)}")
                     
    elif selected_option=="Méthode itérative":
                    operation = st.selectbox("Choisissez la méthode   ", ["Jacobie avec nombre d'itération connnue ", "Jacobie par une valeur approché epsilon","Gauss-Seidel avec nombre d'itération connnue ","Gauss-Seidel par une valeur approché epsilon" ])
                    if operation=="Jacobie avec nombre d'itération connnue " or operation=="Gauss-Seidel avec nombre d'itération connnue ":
                        num_iterations = st.slider("Choisissez un entier supérieur à 2", min_value=2, max_value=100,step=1)
                        st.write("Vous avez choisi le nombre d'itération  :", num_iterations)
                    elif operation=="Jacobie par une valeur approché epsilon" or operation=="Gauss-Seidel par une valeur approché epsilon":
                        epsilon = st.number_input("Veuillez entrer un epsilon (très proche de 0)", min_value=0.000000000000000001, max_value=0.01, step=0.000000000000000001)
                        # Affichez l'epsilon choisi par l'utilisateur
                        st.write("Vous avez choisi epsilon :", epsilon)
                    if st.button("Résoudre"):
                         try:
                             A=np.array(f.get_matrix_values_A(),dtype=float)
                             n=A.shape[0]
                             b=np.array(f.get_vector_values(),dtype=float)
                             if n!=np.size(b):
                                 st.warning("Les dimensions de matrice A et vecteur B doit etre égale")
                                 exit(0)
                             if np.linalg.det(A) == 0:
                                 if np.linalg.norm(b) == 0:
                                   st.warning("Infiniment de solutions ")
                                   exit(0)
                                 else:
                                   st.warning("Aucune solution ")
                                   exit(0)
                             else :
                                 rang_A = np.linalg.matrix_rank(A)
                  
                                 if rang_A != A.shape[1]:
                                     st.warning("Infiniment de solutions ")
                                     exit(0)
                                 if I.Gausse_soleide_converge(A, n)==False or I.Jacobie_converge(A, n)==False:
                                     st.warning("La matrice est diverge")
                                     exit(0)
                             
                             matrix_type = dt.determine_matrix_type(A)
                             st.success(dt.message_info(matrix_type, A))
                             if operation=="Jacobie par une valeur approché epsilon" :
                                 r=I.jacobi_epsilon(A, b, n, epsilon)
                             elif operation=="Jacobie avec nombre d'itération connnue ":
                                 r=I.jacobi_fixed_iterations(A, b, n, num_iterations)
                             elif operation=="Gauss-Seidel avec nombre d'itération connnue ":
                                 r=I.Gauss_Seidel_fixed_iterations(A, b, n, num_iterations)
                             else :
                                 r=I.Gauss_Seidel_epsilon(A, b, n, epsilon)
                            
                             st.dataframe(FR.matrix_to_fraction(r))
                                 
                                
                         except ValueError as e:
                                     st.error(f"Erreur lors de la conversion des données de la matrice A ou B : {str(e)}")
                         except Exception as ex:
                                     st.error(f"Une exception s'est produite lors de la résolution de systéme : {str(ex)}")        
                    
                        
                    
                    
                
                       
                    
                    
            
               
          
                
main() 