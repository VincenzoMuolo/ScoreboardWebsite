import streamlit as st
import pandas as pd

# === Init stato ===
if "page" not in st.session_state:
    st.session_state.page = "Home"

# === Sidebar ===
pages = ["Home", "Classifica", "Regolamento"]
# Escludi la pagina corrente dalla sidebar
other_pages = [p for p in pages if p != st.session_state.page]

# Se c'è più di una pagina alternativa, mostra radio
if other_pages:
    choice = st.sidebar.radio("Naviga a:", other_pages)
    if choice:
        st.session_state.page = choice

# === Dati ===
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

# === Pagine ===
if st.session_state.page == "Home":
    st.markdown("<h1 style='text-align: center;'>Benvenuto!</h1>", unsafe_allow_html=True)
    st.image("logo.png", width=400)
    st.markdown("""
    ## Descrizione
    Questa è la homepage del tuo evento.
    """)
elif st.session_state.page == "Classifica":
    st.markdown("<h1 style='text-align: center;'>Leaderboard</h1>", unsafe_allow_html=True)
    styled_df = df.style.apply(highlight_rows, axis=1)
    st.dataframe(styled_df)
elif st.session_state.page == "Regolamento":
    st.markdown("<h1 style='text-align: center;'>Regolamento Evento</h1>", unsafe_allow_html=True)
    st.markdown("""
    ## Regole
    Qui puoi inserire tutte le regole dell'evento.
    """)
