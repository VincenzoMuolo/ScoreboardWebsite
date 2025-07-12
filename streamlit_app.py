import streamlit as st
import pandas as pd

# === Dati ===
data = {
    "Name": ["ITz.Shadow.", "Marius89", "iPriMoRL", "Leam..", "Doc_-_", "AwayFridish", "Hagn99", "Antax_TM","DIOCANE"],
    "1st": [3, 2, 0, 1, 0, 1, 0, 0, 9],
    "2nd": [2, 1, 2, 0, 0, 1, 1, 0, 9],
    "3rd": [0, 1, 2, 1, 1, 0, 2, 1, 9],
    "4th": [1, 0, 0, 1, 1, 0, 0, 1, 9],
    "5th": [0, 0, 1, 2, 1, 0, 1, 0, 9],
    "6th": [1, 0, 0, 1, 3, 1, 0, 0, 9],
    "7th": [1, 0, 0, 0, 1, 0, 0, 0, 9],
    "8th": [0, 0, 0, 0, 1, 0, 0, 0, 9],
    "Pts": [81, 52, 49, 45, 34, 30, 29, 17, 7900]
}
df = pd.DataFrame(data)
df.index = df.index + 1

# === Evidenzia righe ===
def highlight_rows(row):
    if row.name <= 4:
        return ['background-color: rgba(20, 77, 20, 0.7); color: white'] * len(row)
    elif row.name <= 8:
        return ['background-color: rgba(164, 75, 0, 0.7); color: white'] * len(row)
    else:
        return [''] * len(row)

# === Tabs ===
tab_home, tab_regolamento, tab_classifica = st.tabs(["🏠 Home", "📜 Regolamento", "🏆 Classifica"])

# === HOME ===
with tab_home:
    st.markdown("<h1 style='text-align: center;'>Benvenuto!</h1>", unsafe_allow_html=True)

    # Colonne per centrare e controllare larghezza
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("logo.png", width=600)  # ~50% pagina tipicamente

    st.markdown("""
    ## Descrizione
    Questa è la homepage del tuo evento.
    Qui puoi mettere informazioni generali, un messaggio di benvenuto e dettagli.
    """)

# === REGOLAMENTO ===
with tab_regolamento:
    st.markdown("<h1 style='text-align: center;'>Regolamento Evento</h1>", unsafe_allow_html=True)
    st.markdown("""
    ## Regole
    Qui puoi inserire tutte le regole dell'evento.

    - Regola 1
    - Regola 2
    - Regola 3

    Ricorda di aggiornare le regole quando necessario!
    """)

# === CLASSIFICA ===
with tab_classifica:
    st.markdown("<h1 style='text-align: center;'>Leaderboard</h1>", unsafe_allow_html=True)

    # Contenitore largo per la tabella
    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        styled_df = df.style.apply(highlight_rows, axis=1)
        st.dataframe(
            styled_df,
            use_container_width=True,  # per Streamlit >=1.30 è accettato per st.dataframe
            height=600
        )
