import streamlit as st

def app():

    st.title('Welcome to :blue[Fine-Tuning GenAI]')

    choice = st.selectbox('Login/Signup',['Login','Sign up'])
    if choice =='Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        
        st.button('Login')
    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your unique username')

        st.button('Create my account')
    