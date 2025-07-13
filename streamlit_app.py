from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import base64

st.set_page_config(
    page_title="Random TraCkup",
    page_icon="🎮",  # oppure un file: "logo.png"
    layout="wide",   # optional: "centered" o "wide"
    initial_sidebar_state="collapsed"  # optional
)

# Carica immagine e codifica in base64
file_ = open("logo.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")

# === NAVBAR ORIZZONTALE ===
selected = option_menu(
    menu_title=None,  # Nessun titolo
    options=["Home", "Regolamento", "Classifica"],
    icons=["house", "file-text", "trophy"],
    orientation="horizontal",
    default_index=0,
)

# === Dati Classifica ===
data = {
    "Name": ["ITz.Shadow.", "Marius89", "iPriMoRL", "Leam..", "Doc_-_", "AwayFridish", "Hagn99", "Antax_TM"],
    "1st": [3, 2, 0, 1, 0, 1, 0, 0],
    "2nd": [2, 1, 2, 0, 0, 1, 1, 0],
    "3rd": [0, 1, 2, 1, 1, 0, 2, 1],
    "4th": [1, 0, 0, 1, 1, 0, 0, 1],
    "5th": [0, 0, 1, 2, 1, 0, 1, 0],
    "6th": [1, 0, 0, 1, 3, 1, 0, 0],
    "7th": [1, 0, 0, 0, 1, 0, 0, 0],
    "8th": [0, 0, 0, 0, 1, 0, 0, 0],
    "Pts": [81, 52, 49, 45, 34, 30, 29, 17]
}
df = pd.DataFrame(data)
df.index = df.index + 1

def highlight_rows(row):
    if row.name <= 4:
        return ['background-color: rgba(20, 77, 20, 0.7); color: white'] * len(row)
    elif row.name <= 8:
        return ['background-color: rgba(164, 75, 0, 0.7); color: white'] * len(row)
    else:
        return [''] * len(row)

# === Contenuto dinamico ===
if selected == "Home":

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{data_url}" style="width: 66%;">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    ## Descrizione
    Questa è la homepage del tuo evento.
    """)

elif selected == "Regolamento":
    st.markdown("<h1 style='text-align: center;'>Regolamento</h1>", unsafe_allow_html=True)
    st.markdown("""
    ## Regole
    - Regola 1
    - Regola 2
    - Regola 3
    """)
elif selected == "Classifica":
    st.markdown("<h1 style='text-align: center;'>Leaderboard</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        styled_df = df.style.apply(highlight_rows, axis=1)
        st.dataframe(styled_df, use_container_width=True, height=600)
