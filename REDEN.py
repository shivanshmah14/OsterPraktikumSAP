import streamlit as st
import pyttsx3
import time

st.title("The Yassin Generator")

# User inputs for customization
count_input = st.number_input("How many times should I say it?", min_value=1, max_value=1000, value=10)
name_to_say = st.text_input("Name to repeat:", value="Yassin")

if st.button("Start Speaking"):
    # Initialize the engine
    engine = pyttsx3.init()
    
    # UI feedback
    status_text = st.empty()
    progress_bar = st.progress(0)
    
    for i in range(count_input):
        # Update UI
        current_count = i + 1
        percent_complete = current_count / count_input
        
        status_text.text(f"Speaking {name_to_say}... ({current_count}/{count_input})")
        progress_bar.progress(percent_complete)
        
        # Speech execution
        engine.say(name_to_say)
        engine.runAndWait()
        
    st.success("Done!")
