import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# Configuration de l'application
st.set_page_config(
    page_title="Gestion des Boîtes aux Lettres",
    page_icon="📬",
    layout="wide"
)

export=pd.read_excel("Export.xlsx")
export_bal=export[['Date contrôle', 'Numéro rue', 'Rue', 'CP', 'Ville', 'Secteur',export.columns[54],export.columns[55],export.columns[56],export.columns[57],export.columns[58]]]
export_bal["Adresse"]=export_bal["Rue"]+" - "+export_bal["CP"].astype(str) +" - "+export_bal["Ville"]+ " - ("+export_bal["Secteur"]+")"
df_glob=pd.read_excel("resultats_scraping.xlsx")
df_bal=df_glob[df_glob["Question"]=="Etat des boîtes aux lettres :"]

df = pd.merge(df_bal, export_bal, on="Adresse", how="inner")
# Fonction pour télécharger une image à partir d'une URL
def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


# Fonction pour la page propreté
def page_proprete():
    st.title("🧹 Propreté")
    st.write("Sur cette page, vous pouvez gérer et visualiser les informations liées à la propreté.")

    # Filtrer les données
    conforme = df[df[df.columns[-2]] == "Conforme"]
    non_conforme = df[df[df.columns[-2]] == "Non conforme"]

        # Fonction pour générer le HTML des images en grille
    def generate_image_grid(df_images, label):
        html = """
        <style>
            .image-grid {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }
            .image-grid img {
                width: 30%; /* Taille réduite pour afficher 3 images par ligne */
                height: auto;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
        </style>
        <div class="image-grid">
        """
        for _, row in df_images.iterrows():
            image_url = row["Image"]
            html += f"<img src='{image_url}' alt='{label}'>"
        html += "</div>"
        return html
    
    # Colonnes pour afficher les images
    col1, separator, col2 = st.columns([1, 0.05, 1])

     # Affichage des images conformes
    with col1:
        st.subheader("✅ Conformes")
        html_conforme = generate_image_grid(conforme, "Conforme")
        st.markdown(html_conforme, unsafe_allow_html=True)

    # Ajouter une séparation visuelle dans la colonne centrale
    with separator:
        st.markdown(
            "<div style='width: 2px; height: 100%; background-color: #ccc; margin: auto;'></div>",
            unsafe_allow_html=True
        )

    # Affichage des images non conformes
    with col2:
        st.subheader("❌ Non Conformes")
        html_non_conforme = generate_image_grid(non_conforme, "Non Conforme")
        st.markdown(html_non_conforme, unsafe_allow_html=True)

# Fonction pour la page esthétique
def page_esthetique():
    st.title("🎨 Esthétique")
    st.write("Visualisez les éléments liés à l'esthétique des boîtes aux lettres ici.")

    # Filtrer les données
    conforme = df[df[df.columns[-1]] == "Conforme"]
    non_conforme = df[df[df.columns[-1]] == "Non conforme"]

        # Fonction pour générer le HTML des images en grille
    def generate_image_grid(df_images, label):
        html = """
        <style>
            .image-grid {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }
            .image-grid img {
                width: 30%; /* Taille réduite pour afficher 3 images par ligne */
                height: auto;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
        </style>
        <div class="image-grid">
        """
        for _, row in df_images.iterrows():
            image_url = row["Image"]
            html += f"<img src='{image_url}' alt='{label}'>"
        html += "</div>"
        return html
    
    # Colonnes pour afficher les images
    col1, separator, col2 = st.columns([1, 0.05, 1])

     # Affichage des images conformes
    with col1:
        st.subheader("✅ Conformes")
        html_conforme = generate_image_grid(conforme, "Conforme")
        st.markdown(html_conforme, unsafe_allow_html=True)

    # Ajouter une séparation visuelle dans la colonne centrale
    with separator:
        st.markdown(
            "<div style='width: 2px; height: 100%; background-color: #ccc; margin: auto;'></div>",
            unsafe_allow_html=True
        )

    # Affichage des images non conformes
    with col2:
        st.subheader("❌ Non Conformes")
        html_non_conforme = generate_image_grid(non_conforme, "Non Conforme")
        st.markdown(html_non_conforme, unsafe_allow_html=True)

# Fonction pour la page harmonisation
def page_harmonisation():
    st.title("🔖 Harmonisation des Étiquettes")

    st.write("Affichage des images conformes et non conformes.")

    # Filtrer les données
    conforme = df[df[df.columns[-3]] == "Conforme"]
    non_conforme = df[df[df.columns[-3]] == "Non conforme"]

        # Fonction pour générer le HTML des images en grille
    def generate_image_grid(df_images, label):
        html = """
        <style>
            .image-grid {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }
            .image-grid img {
                width: 30%; /* Taille réduite pour afficher 3 images par ligne */
                height: auto;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
        </style>
        <div class="image-grid">
        """
        for _, row in df_images.iterrows():
            image_url = row["Image"]
            html += f"<img src='{image_url}' alt='{label}'>"
        html += "</div>"
        return html
    
    # Colonnes pour afficher les images
    col1, separator, col2 = st.columns([1, 0.05, 1])

     # Affichage des images conformes
    with col1:
        st.subheader("✅ Conformes")
        html_conforme = generate_image_grid(conforme, "Conforme")
        st.markdown(html_conforme, unsafe_allow_html=True)

    # Ajouter une séparation visuelle dans la colonne centrale
    with separator:
        st.markdown(
            "<div style='width: 2px; height: 100%; background-color: #ccc; margin: auto;'></div>",
            unsafe_allow_html=True
        )

    # Affichage des images non conformes
    with col2:
        st.subheader("❌ Non Conformes")
        html_non_conforme = generate_image_grid(non_conforme, "Non Conforme")
        st.markdown(html_non_conforme, unsafe_allow_html=True)



# Dictionnaire des pages
PAGES = {
    "Propreté": page_proprete,
    "Esthétique": page_esthetique,
    "Harmonisation des étiquettes": page_harmonisation,
}

# Barre latérale pour la navigation
st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("", list(PAGES.keys()))

# Appel de la fonction correspondant à la page sélectionnée
page = PAGES[selection]
page()
