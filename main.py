import streamlit as st
import requests

st.title("Astronomy Photo of the Day")

api_key = st.secrets["api"]["API_KEY"]
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url).json()

st.header(response["title"])
if response["media_type"] == "image":
    if response["hdurl"]:
        st.image(response["hdurl"], use_container_width=True)
    else:
        st.image(response["url"], use_container_width=True)
st.text(response["explanation"])
