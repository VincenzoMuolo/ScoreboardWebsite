import streamlit as st
import pandas as pd

# === Init stato ===
if "page" not in st.session_state:
    st.session_state.page = "Home"

# === Navbar custom ===
st.markdown(
    """
    <style>
    .nav {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
    }
    .nav a {
        margin: 0 15px;
        text-decoration: none;
        color: black;
        font-weight: bold;
        font-size: 18px;
    }
    .nav a:hover {
        color: #FF4B4B;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="nav">
        <a href="?page=Home">🏠 Home</a>
        <a href="?page=Classifica">🏆 Classifica</a>
        <a href="?page=Regolamento">📜 Regolamento</a>
    </div>
    """,
    unsafe_allow_html=True
)

# === Routing ===
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["Home"])[0]

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

# === Contenuto dinamico ===
if page == "Home":
    st.markdown("<h1 style='text-align: center;'>Benvenuto!</h1>", unsafe_allow_html=True)
    st.image("logo.png", width=400)
    st.write("Questa è la homepage.")

elif page == "Classifica":
    st.markdown("<h1 style='text-align: center;'>Leaderboard</h1>", unsafe_allow_html=True)
    styled_df = df.style.apply(highlight_rows, axis=1)
    st.dataframe(styled_df)

elif page == "Regolamento":
    st.markdown("<h1 style='text-align: center;'>Regolamento Evento</h1>", unsafe_allow_html=True)
    st.write("Qui puoi inserire le regole.")
