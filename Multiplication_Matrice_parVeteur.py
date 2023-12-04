import streamlit as st
import numpy as np
import Determinated_Nature_Matrice as dt
import Matrice_Vecteur as MV
import FLASK as f
import Fraction as FR

def app():
    st.header("Multiplication y=Ab")
    matrice_html=f.matriceA_html()
    vecteur_html=f.vecteur_html()
    col1,col2=st.columns(2)
    with col1:
        st.components.v1.html(matrice_html,width=300, height=300)
    with col2:
        st.components.v1.html(vecteur_html,width=300, height=300)

    if st.button("Multiplier"):
       try:
           A=np.array(f.get_matrix_values_A(),dtype=float)
           n=A.shape[0]
           
           b=np.array(f.get_vector_values(),dtype=float)
           if n!=np.size(b):
               st.warning("Les dimensions de matrice A et vecteur B doit etre égale")
               exit(0)
           matrix_type_A = dt.determine_matrix_type(A)
           st.success(dt.message_info(matrix_type_A, A))
               
         
          
           if matrix_type_A=="Triangulaire supérieure":
               result=MV.Matrice_sup(A, b, n)
           elif matrix_type_A=="Triangulaire inférieure": 
               result=MV.Matrice_inf(A, b, n)
           elif matrix_type_A[0]=="demi bande inférieur":
               result=MV.Matrice_demi_bande_inf(A, b, n, matrix_type_A[1])
           elif matrix_type_A[0]=="demi bande supérieur":
               result=MV.Matrice_demi_bande_sup(A, b, n, matrix_type_A[1])
           else:
               result=MV.Matrice_Dense(A, b, n)
           st.success("Résultat de la multiplication de matrices :")
           st.dataframe(FR.matrix_to_fraction(result))

       except ValueError as e:
           st.error(f"Erreur lors de la conversion des données : {str(e)}")
       except Exception as e:
           st.error(f"Une erreur inattendue s'est produite : {str(e)}")
def main():
    app() 
if __name__ == "__main__":
    main()
