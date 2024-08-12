import streamlit as st
import streamlit.components.v1 as com

com.iframe("https://lottie.host/embed/302141c9-8e0f-43bf-9c3f-f17064143684/ytm4nfuHSV.json")

st.title("The Dataset 📊")
url = "https://jadarat.sa/"
st.write("I used a dataset from the 'jadarat' website to do some analysis. 'jadarat' is Saudi Arabia's national employment platform connecting job seekers with opportunities in both public and private sectors​")
st.write("[Check the source](%s)" % url)
st.markdown("---")