import streamlit as st
import pandas as pd

# Sidebar per la "navbar"
page = st.sidebar.radio(
    "Naviga",
    ["🏆 Classifica", "ℹ️ Info Evento"]
)

# === DATI ===
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

# === PAGINE ===
if page == "🏆 Classifica":
    st.title("Leaderboard")
    styled_df = df.style.apply(highlight_rows, axis=1)
    st.dataframe(styled_df, use_container_width=True)

elif page == "ℹ️ Info Evento":
    st.title("Informazioni Evento")
    st.markdown("""
    ## Descrizione
    Benvenuto nella pagina informativa dell'evento!  
    Qui puoi spiegare **regole**, **criteri di punteggio**, **premi**, oppure raccontare come funziona la competizione.
    
    ✨ **Esempio:**  
    > Questa classifica è aggiornata in tempo reale in base ai risultati dei partecipanti.
    >  
    > - Ogni posizione assegna punti diversi.
    > - Le prime 4 posizioni vengono evidenziate in verde.
    > - Dalla 5° alla 8° posizione in arancione.
    
    📌 Puoi personalizzare questa descrizione come vuoi!
    """)