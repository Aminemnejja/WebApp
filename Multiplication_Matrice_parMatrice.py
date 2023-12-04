import streamlit as st
import numpy as np
import Determinated_Nature_Matrice as dt
import Matrice_Matrice as MA
import FLASK as f
import Fraction as FR

def main():
  

    selected_option = st.radio("Sélectionnez une opération", ["Multiplier par une matrice", "Multiplication par inverse de matrice A demi bande", "Multiplication de matrice A par son transposée"])
    matriceA_html=f.matriceA_html()
    matriceB_html=f.matriceB_html()
    if selected_option == "Multiplier par une matrice":
        st.header("Multiplication AB")
     

        col1,col2=st.columns(2)
        with col1:
            st.components.v1.html(matriceA_html,width=500, height=500)
        with col2:
            st.components.v1.html(matriceB_html,width=500, height=500)
        if st.button("Résultat"):
            app_multiply_matrices()

    elif selected_option == "Multiplication par inverse de matrice A demi bande":
        st.header("Multiplication de  A\u207B\u00B9")
        st.components.v1.html(matriceA_html,width=300, height=300)
  

        if st.button("Résultat"):
           
            app_inverse_multiply_band_matrix()

    elif selected_option == "Multiplication de matrice A par son transposée":
        st.header("Multiplication de AAᵀ")
        
        st.components.v1.html(matriceA_html,width=300, height=300)

        if st.button("Résultat"):
            app_multiply_transpose_band_matrix()

def app_multiply_matrices():
    try:
        A =np.array(f.get_matrix_values_A(),dtype=float)
        n = A.shape[0]
        
        matrix_type_A = dt.determine_matrix_type(A)

        B =np.array(f.get_matrix_values_B(),dtype=float)
        if (n!=B.shape[0]):
            st.warning("Les deux matrice  doit etre de méme Taile")
            exit(0)
        matrix_type_B = dt.determine_matrix_type(B)
        st.success(dt.message_info(matrix_type_A, A))
        st.success(dt.message_info(matrix_type_B, B) )  

        if matrix_type_A[0] == "matrice bande" and matrix_type_B[0] == "demi bande inférieur" and matrix_type_A[1] == matrix_type_B[1]:
            result = MA.multiplication_matrice_band_demi_bande(A, B, matrix_type_A[1], n)
            st.success("Résultat de la multiplication de matrices :")
            st.dataframe(FR.matrix_to_fraction(result))
        elif matrix_type_A[0] == "demi bande inférieur" and matrix_type_B[0] == "demi bande supérieur" and matrix_type_A[1] != matrix_type_B[1]:
            result = MA.multiplication_demi_bande_sup_bande(A, B, matrix_type_A[1], matrix_type_B[1], n)
            st.success("Résultat de la multiplication de matrices :")
            st.dataframe(FR.matrix_to_fraction(result))
        else:
            result = MA.multiplication_dense_dense(A, B, n)
            st.success("Résultat de la multiplication de matrices :")
            
            st.dataframe(FR.matrix_to_fraction(result))

    except ValueError as e:
        st.error(f"Erreur lors de la conversion des données de la matrice A ou B : {str(e)}")
    except Exception as ex:
        st.error(f"Une exception s'est produite lors de la multiplication par une matrice : {str(ex)}")


def app_inverse_multiply_band_matrix():
    try:
        A =np.array(f.get_matrix_values_A(),dtype=float)
        if np.linalg.det(A) == 0:
            st.warning("Matrice A n'est pas inversible")
            exit(0)
        n = A.shape[0]
        matrix_type_A = dt.determine_matrix_type(A)
        st.success(dt.message_info(matrix_type_A, A))

        if matrix_type_A[0] == "matrice bande":
            result = MA.multiplication_bande_inverse(A, n, matrix_type_A[1])
            col1, col2 = st.columns(2)
            with col1:
                st.success("Résultat Inverse de matrice:")
                st.dataframe(FR.matrix_to_fraction(result[1]))
            with col2:
                st.success("Résultat de multiplication")
                st.dataframe(FR.matrix_to_fraction(result[0]))
                
        
    except ValueError as e:
        st.error(f"Erreur lors de la conversion des données de la matrice A : {str(e)}")
    except Exception as ex:
        st.error(f"Une exception s'est produite lors de la multiplication par l'inverse d'une matrice bande : {str(ex)}")

def app_multiply_transpose_band_matrix():
    try:
        A =np.array(f.get_matrix_values_A(),dtype=float)

        n = A.shape[0]
        matrix_type_A = dt.determine_matrix_type(A)
        st.success(dt.message_info(matrix_type_A, A))

        if matrix_type_A[0] == "matrice bande":
            result = MA.multiplication_bande_transposer(A, matrix_type_A[1], n)
            st.success("Résultat de la multiplication de matrices par son Transposée :")
            st.dataframe(FR.matrix_to_fraction(result))
        else :
            result=MA.multiplication_dense_dense(A, A.T, n)
            st.success("Résultat de la multiplication de matrices par son Transposée :")
            st.dataframe(FR.matrix_to_fraction(result))

        
    except ValueError as e:
        st.error(f"Erreur lors de la conversion des données de la matrice A : {str(e)}")
    except Exception as ex:
        st.error(f"Une exception s'est produite lors de la multiplication par la transposée d'une matrice bande : {str(ex)}")

if __name__ == "__main__":
    main()