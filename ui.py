import streamlit as st
import requests

st.title('URL Shortner')

#write streamlit for the url shortner
url = st.text_input('Enter the URL')

if st.button('Shorten'):
    response = requests.post("http://localhost:8000/shorten", json={"url": url})
    if response.status_code == 200:
        short_url = response.json().get("short_url")
        st.write(f"Shortened URL: {short_url}")
    else:
        st.write("Some error occurred")