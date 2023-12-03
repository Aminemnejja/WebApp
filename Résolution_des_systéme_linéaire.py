import streamlit as st
import numpy as np
import Determinated_Nature_Matrice as dt
import FLASK as f
import Systeme_Lineaire_Triangulaire as t
import Méthode_direct as m
import Méthode_itérative as I
import Fraction as FR


def display_matrix_with_fractions(matrix, name):
    st.header(name)
    st.dataframe(FR.matrix_to_fraction(matrix))


def resolve_direct_method(A, b, operation, matrix_type):
    if operation == "Gauss":
        if matrix_type[0] == "matrice bande" and np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) > 0):
            A, b = m.elimination_gaussienne_sans_pivot_bande_symetrique(A, b, A.shape[0], matrix_type[1])
            x = t.sys_lin_sup_demiBande(A, b, A.shape[0], matrix_type[1])
            display_matrix_with_fractions(x, "Résultat")
        elif matrix_type == "Symétrique" and np.all(np.linalg.eigvals(A) > 0):
            A, b = m.elimination_gaussienne_sans_pivot_dense_symetrique(A, b, A.shape[0])
            x = t.sys_lin_sup_dense(A, b, A.shape[0])
            display_matrix_with_fractions(x, "Résultat")
        elif matrix_type[0] == "matrice bande":
            A, b = m.elimination_gaussienne_avec_pivot_bande(A, b, A.shape[0], matrix_type[1])
            x = t.sys_lin_sup_demiBande(A, b, A.shape[0], matrix_type[1])
            display_matrix_with_fractions(x, "Résultat")
        else:
            A, b = m.elimination_gaussienne_avec_pivot_dense(A, b, A.shape[0])
            x = t.sys_lin_sup_dense(A, b, A.shape[0])
            display_matrix_with_fractions(x, "Résultat")
    elif operation == "Gauss_jordan":
        b = b[:, np.newaxis]
        if matrix_type[0] == "matrice bande" and np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) > 0):
            x = m.gauss_jordan_bande_symetrique(A, b, A.shape[0], matrix_type[1])
            display_matrix_with_fractions(x, "Résultat")
        elif matrix_type == "Symétrique" and np.all(np.linalg.eigvals(A) > 0):
            x = m.gauss_jordan_dense_symetrique(A, b, A.shape[0])
            display_matrix_with_fractions(x, "Résultat")
        else:
            x = m.gauss_jordan_dense(A, b, A.shape[0])
            display_matrix_with_fractions(x, "Résultat")
    elif operation == "Décomposition LU":
        if matrix_type[0] == "matrice bande" and np.allclose(A, A.T) and np.all(np.linalg.eigvals(A) > 0):
            L, D = m.decomposition_LU_bande_Symetrique(A, A.shape[0], matrix_type[1])
            U = np.dot(D, L.T)
            y = t.sys_lin_inf_demiBande(L, b, A.shape[0], matrix_type[1])
            x = t.sys_lin_sup_demiBande(U, y, A.shape[0], matrix_type[1])
            display_matrix_with_fractions(L, "Matrice L")
            display_matrix_with_fractions(U, "Matrice U")
            display_matrix_with_fractions(x, "Résultat")
        elif matrix_type[0] == "matrice bande" and np.all(np.linalg.eigvals(A) > 0):
            L, U = m.decomposition_LU_bande(A, A.shape[0], matrix_type[1])
            y = t.sys_lin_inf_demiBande(L, b, A.shape[0], matrix_type[1])
            x = t.sys_lin_sup_demiBande(U, y, A.shape[0], matrix_type[1])
            display_matrix_with_fractions(L, "Matrice L")
            display_matrix_with_fractions(U, "Matrice U")
            display_matrix_with_fractions(x, "Résultat")
        elif matrix_type[0] == "Symétrique" and np.all(np.linalg.eigvals(A) > 0):
            L, D = m.decomposition_LU_dense_Symetrique(A, A.shape[0])
            U = np.dot(D, L.T)
            y = t.sys_lin_inf_dense(L, b, A.shape[0])
            x = t.sys_lin_sup_dense(U, y, A.shape[0])
            display_matrix_with_fractions(L, "Matrice L")
            display_matrix_with_fractions(U, "Matrice U")
            display_matrix_with_fractions(x, "Résultat")
        elif np.all(np.linalg.eigvals(A) > 0):
            L, U = m.decomposition_LU_dense(A, A.shape[0])
            y = t.sys_lin_inf_dense(L, b, A.shape[0])
            x = t.sys_lin_sup_dense(U, y, A.shape[0])
            display_matrix_with_fractions(L, "Matrice L")
            display_matrix_with_fractions(U, "Matrice U")
            display_matrix_with_fractions(x, "Résultat")
        else:
            st.error("Matrice doit etre definie positive")


def resolve_iterative_method(A, b, operation, num_iterations, epsilon):
    if operation == "Jacobie par une valeur approché epsilon":
        r = I.jacobi_epsilon(A, b, A.shape[0], epsilon)
    elif operation == "Jacobie avec nombre d'itération connnue":
        r = I.jacobi_fixed_iterations(A, b, A.shape[0], num_iterations)
    elif operation == "Gauss-Seidel avec nombre d'itération connnue":
        r = I.Gauss_Seidel_fixed_iterations(A, b, A.shape[0], num_iterations)
    else:
        r = I.Gauss_Seidel_epsilon(A, b, A.shape[0], epsilon)

    display_matrix_with_fractions(r, "Résultat")
def main():
    st.header("Résolution de systéme : Ax=b")
    selected_option = st.radio("Sélectionnez une méthode", ["Méthode direct", "Méthode itérative"])
    matrice_html = f.matriceA_html()
    vecteur_html = f.vecteur_html()

    col1, col2 = st.columns(2)
    with col1:
        st.components.v1.html(matrice_html, width=300, height=300)
    with col2:
        st.components.v1.html(vecteur_html, width=300, height=300)

    if selected_option == "Méthode direct":
        operation = st.selectbox("Choisissez l'opération ", ["Gauss", "Gauss_jordan", "Décomposition LU", "Cholesky"])

        if st.button("Résoudre"):
            try:
                A = np.array(f.get_matrix_values_A(), dtype=float)
                n = A.shape[0]
                b = np.array(f.get_vector_values(), dtype=float)

                if n != np.size(b):
                    st.warning("Les dimensions de matrice A et vecteur B doivent être égales")
                    exit(0)

                if np.linalg.det(A) == 0:
                    if np.linalg.norm(b) == 0:
                        st.warning("Infiniment de solutions ")
                        exit(0)
                    else:
                        st.warning("Aucune solution ")
                        exit(0)
                else:
                    rang_A = np.linalg.matrix_rank(A)

                    if rang_A != A.shape[1]:
                        st.warning("Infiniment de solutions ")
                        exit(0)

                matrix_type_A = dt.determine_matrix_type(A)
                st.success(f"Type de matrice A détecté : {matrix_type_A}")

                resolve_direct_method(A, b, operation, matrix_type_A)

            except ValueError as e:
                st.error(f"Erreur lors de la conversion des données de la matrice A ou B : {str(e)}")
            except Exception as ex:
                st.error(f"Une exception s'est produite lors de la résolution  de systéme  : {str(ex)}")

    elif selected_option == "Méthode itérative":
        operation = st.selectbox("Choisissez la méthode   ", ["Jacobie avec nombre d'itération connnue ",
                                                              "Jacobie par une valeur approché epsilon",
                                                              "Gauss-Seidel avec nombre d'itération connnue ",
                                                              "Gauss-Seidel par une valeur approché epsilon"])

        if operation in ["Jacobie avec nombre d'itération connnue", "Gauss-Seidel avec nombre d'itération connnue"]:
            num_iterations = st.slider("Choisissez un entier supérieur à 2", min_value=2, max_value=100, step=1)
            st.write("Vous avez choisi le nombre d'itération  :", num_iterations)
        elif operation in ["Jacobie par une valeur approché epsilon", "Gauss-Seidel par une valeur approché epsilon"]:
            epsilon = st.number_input("Veuillez entrer un epsilon (très proche de 0)", min_value=1e-18, max_value=0.01,
                                      step=1e-18)
            # Affichez l'epsilon choisi par l'utilisateur
            st.write("Vous avez choisi epsilon :", epsilon)

        if st.button("Résoudre"):
            try:
                A = np.array(f.get_matrix_values_A(), dtype=float)
                n = A.shape[0]
                b = np.array(f.get_vector_values(), dtype=float)

                if n != np.size(b):
                    st.warning("Les dimensions de matrice A et vecteur B doit etre égale")
                    exit(0)

                if np.linalg.det(A) == 0:
                    if np.linalg.norm(b) == 0:
                        st.warning("Infiniment de solutions ")
                        exit(0)
                    else:
                        st.warning("Aucune solution ")
                        exit(0)
                else:
                    rang_A = np.linalg.matrix_rank(A)

                    if rang_A != A.shape[1]:
                        st.warning("Infiniment de solutions ")
                        exit(0)

                matrix_type_A = dt.determine_matrix_type(A)
                st.success(f"Type de matrice A détecté : {matrix_type_A}")

                resolve_iterative_method(A, b, operation, num_iterations, epsilon)

            except ValueError as e:
                st.error(f"Erreur lors de la conversion des données de la matrice A ou B : {str(e)}")
            except Exception as ex:
                st.error(f"Une exception s'est produite lors de la résolution  de systéme  : {str(ex)}")


main()