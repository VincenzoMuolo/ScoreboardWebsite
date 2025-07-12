import streamlit as st
import pandas as pd

# === Imposta pagina iniziale ===
if "page" not in st.session_state:
    st.session_state.page = "Home"

# === Sidebar verticale ===
pages = ["Home", "Regolamento", "Classifica"]
page = st.sidebar.radio("Naviga:", pages)
st.session_state.page = page

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

# === Contenuto ===
if st.session_state.page == "Home":
    st.markdown("<h1 style='text-align: center;'>Benvenuto!</h1>", unsafe_allow_html=True)

    # Layout centrato con larghezza ~50% pagina
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", use_container_width=True)

    st.markdown("""
    ## Descrizione
    Benvenuto alla homepage del tuo evento.
    Qui puoi mettere info generali e un messaggio di benvenuto.
    """)

elif st.session_state.page == "Regolamento":
    st.markdown("<h1 style='text-align: center;'>Regolamento Evento</h1>", unsafe_allow_html=True)
    st.markdown("""
    ## Regole
    Qui puoi inserire tutte le regole dell'evento:

    - Regola 1
    - Regola 2
    - Regola 3

    Aggiorna le regole quando necessario!
    """)

elif st.session_state.page == "Classifica":
    st.markdown("<h1 style='text-align: center;'>Leaderboard</h1>", unsafe_allow_html=True)

    # Layout centrato con larghezza ~80% pagina
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        styled_df = df.style.apply(highlight_rows, axis=1)
        st.dataframe(
            styled_df,
            use_container_width=True,
            height=600
        )
