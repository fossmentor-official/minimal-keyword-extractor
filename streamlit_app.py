import streamlit as st
from extractor import extract_keywords

st.title("🧠 Minimal Keyword Extractor")

text = st.text_area("Paste your text here...")
top_k = st.slider("Number of keywords:", 5, 20, 10)

if st.button("Extract"):
    if text.strip():
        result = extract_keywords(text, top_k)
        st.write("### Top Keywords:")
        for word, score in result:
            st.write(f"• **{word}** — {round(score, 4)}")
    else:
        st.warning("Please enter some text.")