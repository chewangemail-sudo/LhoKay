Import streamlit as st 
Import os 
From modules.translator import load_dataset, search_word, log_missing_word 
From modules.quiz import get_quiz_question 
 
# ---------- PAGE SETUP ---------- 
St.set_page_config(page_title=”Lhokay”, page_icon=” 
 
 
 
 
  ”, layout=”centered”) 
 
# ---------- LOAD DATASET ---------- @st.cache_data 
Def get_data(): 
    Return load_dataset(“bhutia_data.csv”) 
 
Try: 
    Df = get_data() 
Except Exception: 
    St.error(“   Could not load dataset. Make sure ‘bhutia_data.csv’ exists.”) 
    St.stop() 
 
# ---------- HEADER ---------- St.title(“ Lhokay
 
 
 
 
  ”) St.markdown(LhoKay Digital Bridge for Sikkim’s Bhutia Language”) 
St.caption(“INSPIRE MANAK Project | Class XII | [chewang], [kewzing]”) 
 
# ---------- TABS ---------- 
Tab_translate, tab_quiz, tab_about = st.tabs( 
    [“ 
 
 
 
 
 
   Translate”, “ 
 
 
   Quiz Mode”, “ 
   About”] 
) 
 
# ---------- TAB 1 : TRANSLATE ---------- 
With tab_translate: 
    Query = st.text_input(“Type an English or Nepali word/phrase:”) 
 
    If query.strip():         Results = search_word(query, df) 
 
        If results: 
            For row in results: 
                St.success(f”**Match:** {row[‘english’]} / {row[‘nepali’]}”) 
                St.markdown(f”## Bhutia: {row[‘bhutia_script’]}”) 
                St.markdown(f”**Pronunciation:** {row[‘transliteration’]}”) 
 
                # Play audio if it exists 
                Audio_path = str(row.get(‘audio’, ‘’)) 
                If audio_path and os.path.exists(audio_path): 
                    St.audio(audio_path) 
        Else: 
            Log_missing_word(query.strip()) 
            St.warning(“ 
 
 
 
 
 
 
   Not found. Added to our wish-list for future data collection!”) 
 
# ---------- TAB 2 : QUIZ MODE ---------- 
With tab_quiz: 
    St.markdown(“Test your Bhutia knowledge!”) 
 
    If st.button(“Get a question”):         Sample, correct, options = get_quiz_question(df) 
        St.session_state[‘quiz’] = { 
            ‘sample’: sample, 
            ‘correct’: correct, 
            ‘options’: options 
        } 
 
    If ‘quiz’ in st.session_state:         Q = st.session_state[‘quiz’] 
        St.write(f”What is the English meaning of **{q[‘sample’][‘bhutia_script’]}**?”) 
        St.caption(f”(Pronunciation hint: {q[‘sample’][‘transliteration’]})”) 
 
        Choice = st.radio(“Choose the correct answer:”, q[‘options’]) 
        If st.button(“Check answer”): 
            If choice == q[‘correct’]: 
                St.success(“ 
   Correct! Well done.”) 
            Else: 
                St.error(f”   Wrong. The correct answer was: {q[‘correct’]}”) 
 
# ---------- TAB 3 : ABOUT ---------- 
With tab_about: 
    St.markdown(f””” 
 **Bhutia Setu** is a foundational digital project to preserve Sikkim’s 
    Endangered Bhutia language. 
 
    * **Dataset entries:** {len(df)} words     * **Built by:** [Your Name], Class XII 
    * **School:** [Your School], Sikkim 
    * **Under:** INSPIRE MANAK Scheme 
 
    This project creates a verified dataset + a beginner-level translation 
    Tool, designed to grow into advanced AI for Bhutia in the future. 
    “””) 