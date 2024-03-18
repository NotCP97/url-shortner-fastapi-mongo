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
        try:
            response_json = response.json().get("detail")[0].get("msg")
            st.write(f"Some error occurred while shortening the URL: {response_json}")
        except:
            st.write("Some error occurred while shortening the URL")