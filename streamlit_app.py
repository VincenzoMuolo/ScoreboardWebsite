import streamlit as st
import pandas as pd

# === Sidebar come navbar ===
page = st.sidebar.radio(
    "Naviga",
    ["🏠 Home", "🏆 Classifica", "📜 Regolamento"]
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
if page == "🏠 Home":
    st.markdown("<h1 style='text-align: center;'>Random TraCkup</h1>", unsafe_allow_html=True)

    st.image("logo.png", use_container_width=True)  # logo grande

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📜 Vai al Regolamento"):
            st.session_state['page'] = "📜 Regolamento"
    
    with col2:
        if st.button("🏆 Vai alla Classifica"):
            st.session_state['page'] = "🏆 Classifica"

elif page == "🏆 Classifica":
    st.title("Leaderboard")
    styled_df = df.style.apply(highlight_rows, axis=1)
    st.dataframe(styled_df, use_container_width=True)

elif page == "📜 Regolamento":
    st.title("Regolamento Evento")
    st.markdown("""
    ## Regole
    Qui puoi inserire tutte le regole dell'evento.
    
    - Dettaglio 1
    - Dettaglio 2
    - Dettaglio 3

    Buona fortuna a tutti i partecipanti!
    """)
