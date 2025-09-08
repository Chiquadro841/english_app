import streamlit as st
import pandas as pd

# ---- Sample Data ----
phrasal_verbs = pd.DataFrame({
    "Italian": ["andare avanti", "dare su", "mettere da parte"],
    "English": ["carry on", "look out onto", "put aside"]
})

words_adjectives = pd.DataFrame({
    "Italian": ["bello", "veloce", "felice"],
    "English": ["beautiful", "fast", "happy"]
})

# ---- Streamlit App ----
st.set_page_config(page_title="English Learning App", layout="wide")

st.title("📚 English Phrasal Verbs & Vocabulary")

# ---- Menu ----
menu = st.selectbox("Choose category:", ["Phrasal Verbs", "Words & Adjectives"])

# ---- Function to show table with hidden translations ----
def show_table(df):
    for idx, row in df.iterrows():
        col1, col2 = st.columns([2, 1])
        col1.write(f"**{row['Italian']}**")
        # Hidden English word with button
        if col2.button("👁️", key=f"{idx}-{row['Italian']}"):
            col2.success(row["English"])
        else:
            col2.write("")

# ---- Display table based on menu selection ----
if menu == "Phrasal Verbs":
    show_table(phrasal_verbs)
elif menu == "Words & Adjectives":
    show_table(words_adjectives)
