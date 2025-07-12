import streamlit as st
import pandas as pd

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

# === Stato iniziale ===
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

# === Home ===
if st.session_state.page == "🏠 Home":
    st.markdown("<h1 style='text-align: center;'>Benvenuto!</h1>", unsafe_allow_html=True)
    st.image("logo.png", use_column_width=True)

    # Crea colonne vuote per centrare
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        go_regolamento = st.button("📜 Vai al Regolamento")
        go_classifica = st.button("🏆 Vai alla Classifica")

    if go_regolamento:
        st.session_state.page = "📜 Regolamento"
    elif go_classifica:
        st.session_state.page = "🏆 Classifica"

# === Pagine interne ===
else:
    # Navbar orizzontale simulata con Tabs
    tabs = st.tabs(["🏆 Classifica", "📜 Regolamento"])
    if tabs[0]:
        if st.session_state.page == "🏆 Classifica":
            st.title("Leaderboard")
            styled_df = df.style.apply(highlight_rows, axis=1)
            st.dataframe(styled_df, use_container_width=True)

    if tabs[1]:
        if st.session_state.page == "📜 Regolamento":
            st.title("Regolamento Evento")
            st.markdown("""
            ## Regole
            Qui puoi inserire tutte le regole dell'evento.

            - Dettaglio 1
            - Dettaglio 2
            - Dettaglio 3

            Buona fortuna a tutti i partecipanti!
            """)

    # Sincronizza tab con session state
    selected_tab = tabs[0] if st.session_state.page == "🏆 Classifica" else tabs[1]