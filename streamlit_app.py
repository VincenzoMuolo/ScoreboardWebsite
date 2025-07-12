import streamlit as st
import pandas as pd

# === Dati di esempio ===
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

# === Stile righe ===
def highlight_rows(row):
    if row.name <= 4:
        return ['background-color: rgba(20, 77, 20, 0.7); color: white'] * len(row)
    elif row.name <= 8:
        return ['background-color: rgba(164, 75, 0, 0.7); color: white'] * len(row)
    else:
        return [''] * len(row)

# === Navbar orizzontale con Tabs ===
tabs = st.tabs(["🏠 Home", "🏆 Classifica", "📜 Regolamento"])

# === Home ===
with tabs[0]:
    st.markdown("<h1 style='text-align: center;'>Benvenuto!</h1>", unsafe_allow_html=True)
    st.image("logo.png", use_column_width=True)
    st.markdown("""
    ## Descrizione
    Questa è la pagina iniziale del tuo evento.  
    Puoi inserire una descrizione, un messaggio di benvenuto o altre info generali.
    """)

# === Classifica ===
with tabs[1]:
    st.title("Leaderboard")
    styled_df = df.style.apply(highlight_rows, axis=1)
    st.dataframe(styled_df, use_container_width=True)

# === Regolamento ===
with tabs[2]:
    st.title("Regolamento Evento")
    st.markdown("""
    ## Regole
    Qui puoi inserire tutte le regole dell'evento.

    - Dettaglio 1
    - Dettaglio 2
    - Dettaglio 3

    Buon divertimento a tutti!
    """)
