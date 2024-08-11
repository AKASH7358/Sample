import streamlit as st

about_page = st.Page(
    "Views/about.py",
    title="About",
    icon=":material/account_circle:",
    default=True,
)
moodboard_page = st.Page(
    "Views/moodboard.py",
    title="Moodboard",
    icon=":material/image:",
)
#project_2_page = st.Page(
#    "views/chatbot.py",
#    title="Chat Bot",
 ##   icon=":material/smart_toy:",
#)

pg = st.navigation(
    {
        "Info": [about_page],
        "Project": [moodboard_page],
    }
)
pg.run()
