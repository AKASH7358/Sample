import streamlit as st
#import os
from streamlit_option_menu import option_menu

#from dotenv import load_dotenv
#load_dotenv()

import About, Account, Moodboard

st.set_page_config(
    page_title = "Fine-Tuning GenAI",
)

class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self,title,function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title="Fine-tuning GenAI",
                options=['About','Moodboard','Account'],
                icons=['chat-fill','image-fill','person-circle'],
                menu_icon='chat-text-fill',
                default_index=1,
                 styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}

                )

        if app=='About':
             About.app()
        if app=='Moodboard':
             Moodboard.app()
        if app=='Account':
             Account.app()
    run()




