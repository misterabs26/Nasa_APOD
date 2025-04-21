import streamlit as st
import requests
from datetime import datetime

from streamlit import divider

st.title("Astronomy Photo of the Day")
st.divider()

# Date input
selected_date = st.date_input("Choose a date",
                              min_value=None,
                              max_value=datetime.today())

if selected_date:
    formatted_date = selected_date.strftime("%Y-%m-%d")

    api_key = st.secrets["api"]["API_KEY"]
    url = (f"https://api.nasa.gov/planetary/apod?api_key={api_key}&"
           f"date={formatted_date}")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        st.header(data["title"],divider="rainbow")

        if data["media_type"] == "image":
            # when hd quality is available
            if data["hdurl"]:
                st.image(data["hdurl"], use_container_width=True)
            else:
                st.image(data["url"], use_container_width=True)
        else:
            st.video(data["url"])

        st.write(data["explanation"])
