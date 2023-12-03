import streamlit as st
from streamlit_option_menu import option_menu
import Multiplication_Matrice_parMatrice as p
import Multiplication_Matrice_parVeteur as v
import Résolution_des_systéme_linéaire as R
# Définir la configuration de la page
st.set_page_config(
        page_title="Calculatrice Matricielle",
        page_icon="🔢",
        layout="wide"
    )


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func, icon="🔢"):
        self.apps.append({
            "title": title,
            "function": func,
            "icon": icon
        })

    def run(self):
        # En-tête de la page
        st.title("Calculatrice Matricielle")

        # Division de la page en colonnes pour le menu et le contenu
        col_menu, col_content = st.columns([2, 3])

        # Section du menu
        with col_menu:
            st.title("Menu")
            # Option de menu avec icônes
            app = option_menu(
                menu_title='Sélectionnez une opération',
                options=["Multiplication de Matrices par Matrice", "Multiplication de Matrices par Vecteur",
                         "Résolution de Systèmes Linéaires"],
                menu_icon='🧮',
                default_index=1,
                styles={
                    "container": {"padding": "10px", "background-color": '#ffffff'},  # Couleur de fond du menu
                    "icon": {"color": "#FFD700", "font-size": "30px", "margin-bottom": "10px"},  # Couleur et taille de l'icône
                    "nav-link": {"color": "#000000", "font-size": "18px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#61b9f0"},  # Couleur et taille des liens du menu
                    "nav-link-selected": {"background-color": "#2285b2"},
                }
            )

        # Section du contenu principal
        with col_content:
            # Boucle sur les applications disponibles
            for a in self.apps:
                if app == a["title"]:
                    # Affichage de l'icône correspondante à l'application
                    st.markdown(f'<div style="font-size: 40px; margin-bottom: 20px; color: #FFD700">{a["icon"]}</div>', unsafe_allow_html=True)
                    # Exécution de la fonction associée à l'application
                    a["function"]()

# Création d'une instance de MultiApp
multi_app = MultiApp()
# Ajout des applications à l'instance
multi_app.add_app("Multiplication de Matrices par Vecteur", v.main)
multi_app.add_app("Multiplication de Matrices par Matrice", p.main)
multi_app.add_app("Résolution de Systèmes Linéaires", R.main)


# Ajoutez d'autres applications si nécessaire

# Exécution de l'application MultiApp
multi_app.run()
