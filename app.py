import streamlit as st
import pandas as pd
import os

# ---- Config ----
st.set_page_config(page_title="English Learning App", layout="wide")
st.title("📚 English Phrasal Verbs & Vocabulary")

# ---- File CSV ----
FILES = {
    "Phrasal Verbs": "phrasal_verbs.csv",
    "Words & Adjectives": "words_adjectives.csv"
}

# ---- Carica CSV (crea se non esiste) ----
def load_csv(path):
    if not os.path.exists(path):
        df = pd.DataFrame(columns=["Italian", "English"])
        df.to_csv(path, index=False, encoding="utf-8")
    return pd.read_csv(path)

# ---- Salva nuova riga ----
def add_row(path, italian, english):
    df = pd.read_csv(path)
    new_row = pd.DataFrame([[italian, english]], columns=["Italian", "English"])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(path, index=False, encoding="utf-8")

# ---- Menu con larghezza limitata ----
st.markdown(
    """
    <style>
    div.stSelectbox {max-width: 300px;}
    </style>
    """,
    unsafe_allow_html=True
)

menu = st.selectbox("Scegli categoria:", list(FILES.keys()))

# ---- Form per aggiungere nuova parola ----
st.subheader("➕ Aggiungi nuova parola")
with st.form("add_word_form"):
    col1, col2 = st.columns(2)
    italian_word = col1.text_input("Italiano")
    english_word = col2.text_input("Inglese")
    submitted = st.form_submit_button("Aggiungi")
    if submitted and italian_word and english_word:
        add_row(FILES[menu], italian_word, english_word)
        st.success(f"✅ Aggiunto: {italian_word} → {english_word}")

# ---- Mostra tabella ----
def show_table(df):
    for idx, row in df.iterrows():
        st.write(f"**{row['Italian']}**")
        key = f"{idx}-{row['Italian']}"
        if st.button("👁️ Mostra traduzione", key=key):
            st.info(row["English"])

df = load_csv(FILES[menu])
show_table(df)


