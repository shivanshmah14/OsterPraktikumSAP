import streamlit as st
from gtts import gTTS
import os

st.title("Yassin's Speaker App")

# Let the user choose the count
count = st.number_input("How many times?", min_value=1, max_value=50, value=5)

if st.button("Start Speaking"):
    # We create one long text string with the name repeated
    full_text = " ".join(["Yassin"] * int(count))
    
    with st.spinner("Preparing audio..."):
        # Generate the audio
        tts = gTTS(text=full_text, lang='en')
        tts.save("speech.mp3")
        
    # Show the audio player and play it automatically
    st.audio("speech.mp3", format="audio/mp3", autoplay=True)
    st.success(f"Finished saying Yassin {count} times!")
