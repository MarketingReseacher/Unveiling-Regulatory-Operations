import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.sidebar.markdown("# Investigation Variables")


@st.cache_resource
def ReadData():
  Data = pd.read_csv('Invs.csv')
  return Data

Data = ReadData()

def GetLabels(x):  
    if x == "InvestigationType":
        Label = "Investigation Type"
    return Label

def labeling(val):
    return f'{val / 100 * len(Data):.0f}\n{val:.0f}%'

def PlotPie(Data, var):
    label = GetLabels(var)
    fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 5))
    Data.groupby(var).size().plot(kind='pie', autopct=labeling, colors=["#C00000", '#FF9999', '#00CCCC', '#49D845', '#CCCC00', '#808080'], textprops={'fontsize': 10}, ax=ax1)
    ax1.set_title(f'Pie Chart of {var}')
    return fig

Selected_var = st.sidebar.selectbox("Select an investigations variable", ["InvestigationType"])
Selected_graph = st.sidebar.selectbox("Select a graph", ["Histogram", "Boxplot", "Pie"])

if Selected_graph == "Pie":
  if Selected_var == "InvestigationType":
    PlotPie(Data, 'InvestigationType')
  st.pyplot(plt) 
