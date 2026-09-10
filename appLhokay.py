import streamlit as st
import os
from modules.translator import load_dataset, search_word, log_missing_word
from modules.quiz import get_quiz_question

st.set_page_config(page_title="Lhokay", layout="centered")

@st.cache_data
def get_data():
    return load_dataset("bhutia_data.csv")

try:
    df = get_data()
except Exception:
    st.error("Could not load dataset. Make sure bhutia_data.csv exists.")
    st.stop()

st.title("Lho-Kay")
st.markdown("A Digital Bridge for Sikkim's Bhutia Language")
st.caption("INSPIRE MANAK Project | Ms. Angela Bhutia Class XII | Jointly developed Mr. Chewang Chopel Bhutia (PGT Physics) and Mr. Karma Tashi Bhutia (PGT Bhutia) | Kewzing SSS")

tab_translate, tab_quiz, tab_about = st.tabs(["Translate", "Quiz Mode", "About"])

with tab_translate:
    query = st.text_input("Type an English or Nepali word/phrase:")
    if query.strip():
        results = search_word(query, df)
        if results:
            for row in results:
                st.success("Match: " + str(row['english']) + " / " + str(row['nepali']))
                st.markdown(" Bhutia: " + str(row['bhutia_script']))
                st.markdown("Pronunciation: " + str(row['transliteration']))
                audio_path = str(row.get('audio', ''))
                if audio_path and os.path.exists(audio_path):
                    st.audio(audio_path)
        else:
            log_missing_word(query.strip())
            st.warning("Not found. Added to our wish-list!")

with tab_quiz:
    st.markdown("Test your Bhutia knowledge!")
    if st.button("Get a question"):
        sample, correct, options = get_quiz_question(df)
        st.session_state['quiz'] = {
            'sample': sample,
            'correct': correct,
            'options': options
        }
    if 'quiz' in st.session_state:
        q = st.session_state['quiz']
        st.write("What is the English meaning of " + str(q['sample']['bhutia_script']) + "?")
        st.caption("(Pronunciation hint: " + str(q['sample']['transliteration']) + ")")
        choice = st.radio("Choose the correct answer:", q['options'])
        if st.button("Check answer"):
            if choice == q['correct']:
                st.success("Correct! Well done.")
            else:
                st.error("Wrong. The correct answer was: " + str(q['correct']))

with tab_about:
    st.markdown("Bhutia Setu is a foundational digital project to preserve Sikkim's endangered Bhutia language.")
    st.write("Total dataset entries: " + str(len(df)))