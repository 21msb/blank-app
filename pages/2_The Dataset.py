import streamlit as st

st.title("Our Dataset 📊")
url = "https://www.kaggle.com/datasets/raihanmuhith/saudi-arabia-used-car/data"
st.write("We used a dataset from the 'Sayara' website to do some analysis. 'Sayara' is a website affiliated with a Saudi company with a commercial registration of 1010538980, based in Riyadh, specializing in selling new cars and guaranteed used cars. The website's services cover all regions of the Kingdom.")
st.write("[Check the Dataset](%s)" % url)
st.markdown("---")