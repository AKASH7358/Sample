import streamlit as st
import pandas as pd
import numpy as np

st.title("Fine-tuning GenAI Project")

st.image("https://img.freepik.com/free-psd/moodboard-with-home-decorations_23-2148394192.jpg?size=626&ext=jpg&ga=GA1.1.1903664533.1722931601&semt=ais_hybrid")
#st.image("./assets/profile_image.png", width=230)

df = pd.DataFrame(
    ["Create a fashion moodboard for men, featuring a camouflage trench coat over a neutral-toned outfit with leather boots. Incorporate urban and woodland settings to emphasize the sophisticated and adventurous spirit of camouflage style.",
"Design a fashion moodboard for men with a camouflage trench coat, neutral-toned outfit, and leather boots. Use urban and woodland settings to highlight the sophisticated spirit of camouflage style.",
"Men’s fashion moodboard: camouflage trench coat, neutral outfit, leather boots. Urban and woodland settings.",
"Camouflage style: trench coat, neutral outfit, leather boots. Urban and woodland.",
"Camouflage style: trench coat, neutral outfit, leather boots."]
)

st.subheader = "Prompts"
# Initialize session state for the DataFrame if it doesn't exist
if 'df' not in st.session_state:
    st.session_state.df = df

# Display the table for editing
edited_df = st.data_editor(st.session_state.df)

# Save button to confirm changes
if st.button("Save changes"):
    # Update the DataFrame in session state with the edited one
    st.session_state.df = edited_df
    st.success("Changes saved!")

# Display the edited (or original) DataFrame
st.write("DataFrame:")
st.table(st.session_state.df)


