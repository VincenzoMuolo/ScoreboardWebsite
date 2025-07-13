from streamlit_option_menu import option_menu
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import pandas as pd
import gspread  # <-- Questo è l'unico pacchetto che serve per Google Sheets
import base64

# === CONFIG ===
st.set_page_config(
    page_title="Random TraCkup",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === Carica logo ===
file_ = open("logo.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")

# === NAVBAR ORIZZONTALE ===
selected = option_menu(
    menu_title=None,
    options=["Home", "Regolamento", "Classifica"],
    icons=["house", "file-text", "trophy"],
    orientation="horizontal",
    default_index=0,
)

# === Autenticazione Google Sheets ===
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["google_drive_API_service_account"],
    scope
)

client = gspread.authorize(creds)

# === Apri Google Sheets ===
spreadsheet = client.open("ClassificaRandomTraCkup")  # Titolo esatto del Google Sheets
worksheet = spreadsheet.worksheet("Classifica")       # Nome del tab

# === Leggi dati ===
data = worksheet.get_all_records()
df = pd.DataFrame(data)

df = df.sort_values(by='Pts', ascending=False)
df.index = range(1, len(df) + 1)
df.index.name = 'Posizione'

# Leggi i dati dalla seconda tab per prendere i testi da inserire nelle varie pagine
contents_sheet = spreadsheet.worksheet("Testi dinamici")
contents_data = contents_sheet.get_all_records()
contents_dict = {row['Chiave']: row['Valore'] for row in contents_data}

# === Evidenzia righe ===
def highlight_rows(row):
    if row.name <= 4:
        return ['background-color: rgba(20, 77, 20, 0.7); color: white'] * len(row)
    elif row.name <= 8:
        return ['background-color: rgba(164, 75, 0, 0.7); color: white'] * len(row)
    else:
        return [''] * len(row)

# === Pagine ===
descrizione = contents_dict.get("descrizione_home", "Inserisci qui i dati dell'evento")
regolamento = contents_dict.get("regolamento", "Info sul regolamento")
regola_1 = contents_dict.get("regola_1", "")
regola_2 = contents_dict.get("regola_2", "")
regola_3 = contents_dict.get("regola_3", "")
regola_4 = contents_dict.get("regola_4", "")
regola_5 = contents_dict.get("regola_5", "")
if selected == "Home":
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{data_url}" style="width: 50%;">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div style='text-align: left; max-width: 800px; margin: 0 auto;'>
            <h2>Descrizione</h2>
            <p>{descrizione}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

elif selected == "Regolamento":
    st.markdown(
        """
        <div style='text-align: left; max-width: 800px; margin: 0 auto;'>
            <h2>Regole</h2>
            <h4>{regolamento}</h4>
            <ul style='list-style-position: inside; text-align: left; display: inline-block;'>
                <li>{regola_1}</li>
                <li>{regola_2}</li>
                <li>{regola_3}</li>
                <li>{regola_4}</li>
                <li>{regola_5}</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

elif selected == "Classifica":
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        styled_df = df.style.apply(highlight_rows, axis=1)
        st.dataframe(
            styled_df,
            use_container_width=True,
            height=720  # altezza in pixel
        )

