import streamlit as st
import random

st.title("AI Music Generator 🎵")

# Define simple music notes
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Button to generate melody
if st.button("Generate Music"):
    melody = [random.choice(notes) for _ in range(8)]
    st.write("Your Melody:", '  '.join(melody))
