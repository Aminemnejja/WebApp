import streamlit as st
import numpy as np
import Determinated_Nature_Matrice as dt
import FLASK as f
import Systeme_Lineaire_Triangulaire as t
import Méthode_direct as m
import Fraction as FR
def main():
    st.header(" Résolution de systéme : Ax=b")
    selected_option = st.radio("Sélectionnez une méthode", ["Méthode direct" ,"Méthode itérative" ])
    matrice_html=f.matriceA_html()
    vecteur_html=f.vecteur_html()
    col1,col2=st.columns(2)
    with col1:
        st.components.v1.html(matrice_html,width=300, height=300)
    with col2:
        st.components.v1.html(vecteur_html,width=300, height=300)
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
                st.success(f"Type de matrice A détecté : {matrix_type_A}")
    
                if operation=="Gauss":
                    if matrix_type_A[0]=="matrice bande" and np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) > 0) :
                        A,b=m.elimination_gaussienne_sans_pivot_bande_symetrique(A, b,n, m)
                        x=t.sys_lin_sup_demiBande(A, b, n, matrix_type_A[1])
                        st.dataframe(FR.matrix_to_fraction(x))
                        
                    elif matrix_type_A=="Symétrique" and np.all(np.linalg.eigvals(A) > 0):
                        A,b=m.elimination_gaussienne_sans_pivot_dense_symetrique(A, b, n)
                        x=t.sys_lin_sup_dense(A, b, n)
                        st.dataframe(FR.matrix_to_fraction(x))
                    elif matrix_type_A[0]=="matrice bande" :
                        A,b=m.elimination_gaussienne_avec_pivot_bande(A, b, n, matrix_type_A[1])
                        x=t.sys_lin_sup_demiBande(A, b, n, matrix_type_A[1])
                        st.dataframe(FR.matrix_to_fraction(x))
                    else:
                        A,b=m.elimination_gaussienne_avec_pivot_dense(A, b, n)
                        x=t.sys_lin_sup_dense(A, b, n)
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
                    st.header("A=L.U")
                    if matrix_type_A[0]=="matrice bande"  :
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
                    else  :
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
    
                
                elif operation=="Cholesky":
                    st.header("A=L.(LT)")
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
                     st.error(f"Une exception s'est produite lors de la multiplication par une matrice : {str(ex)}")

                    
                    
                    
            
               
          
                
main()