import streamlit as st

st.set_page_config(
    page_title="Clustering App",
    page_icon="🧩",
)
st.markdown(
    """
    <style>
    body *{
    text-align:center;
    }
        img{
        margin:30px 0;
        border-radius:100%;
        align-self:center;
        }
        .content{
        align-self:center;
        text-align:center;
        }
        .head{
        margin-top:30px;
        color:#138d75 !important;
        }
        .filiere{
        }
        .annee{
        }
        @media (max-width:567px){
            .head{
                margin-top: 0px
        }
        }
    </style>
    """, unsafe_allow_html=True
)

st.title("HomePage")
st.header("“Doesn't matter how much data you have, it's whether you use it successfully that counts.”")
image_path= "Profile.png"
col21, col22 = st.columns(2)

with col21:
    st.image(image_path,width=250)

with col22:
    st.markdown("""<div class="content">
                <h1 class="head">Ziad Ouahbi</h1>
                <h3 class="filiere">Filière : FID1</h3>
                <h3 class="annee">Année Universitaire : 2023/2024</h3>
                </div>""",unsafe_allow_html=True)


st.title("Rapport Du Projet")

def get_pdf_file_data(file_path):
    """Read binary file and convert it to b64 for download."""
    with open(file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    return pdf_bytes

# Path to your PDF file
pdf_path = 'Rapport Projet.pdf'

# Get PDF file data
pdf_file_data = get_pdf_file_data(pdf_path)

# Streamlit download button
st.download_button(
    label="Télécharger le rapport",
    data=pdf_file_data,
    file_name="Rapport Projet.pdf",
    mime="application/octet-stream"
)
