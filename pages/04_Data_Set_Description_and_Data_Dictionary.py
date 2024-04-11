import numpy as np
import pandas as pd
import streamlit as st

st.sidebar.markdown("# Dictionary")


@st.cache_resource
def ReadData():
  Data = pd.read_csv('Dictionary.csv')
  return Data

st.markdown("#### Our data retrieval and data set construction procedure")
st.image("Picture3.jpg")

Data = ReadData()
st.write(Data.head(5))
Dic = Data.to_csv(encoding='utf-8', index=False)
st.download_button('Download dictionary', Dic, file_name='Dictionary.csv')