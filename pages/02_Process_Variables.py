import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.sidebar.markdown("# Process Variables")


@st.cache_resource
def ReadData():
  Data = pd.read_csv('Outcomes.csv')
  return Data

Data = ReadData()

def GetColors(x):  
    if x == "First Complaint to Investigation Opening":
        Color = "#8FAADC"
    elif x == "Investigation Opening to Closing":
        Color = "#7030A0"
    elif x == "Investigation Closing to Recall":
        Color = "#C00000"
    elif x == "Manufacturer Awareness to Recall":
        Color = "#3b8254"  
    else:
        Color = "#FFC000"
    return Color


def PlotHist(x, var):
    fig, ax = plt.subplots()
    Color = GetColors(var)    
    plt.hist(x,  color=Color)
    plt.title(f'Histogram of {var}', size=12)
    plt.xlabel(var, size=10, style= "italic")
    plt.ylabel("Frequency", size=12)
    fig.set_figheight(6)
    fig.set_figwidth(8)
    return fig



def PlotBox(x, var):
    fig, ax = plt.subplots()
    x = x.dropna()
    plt.boxplot(x,  patch_artist=True)
    plt.title(f'Boxplot of {var}', size=12)
    plt.ylabel(var, size=12, style= "italic")
    fig.set_figheight(6)
    fig.set_figwidth(8)
    return fig
    

Labels = {'FirstComplaintToInvOpening': "First Complaint to Investigation Opening",  'InvOpeningToClosing': "Investigation Opening to Closing", 'InvClosingToRecall': "Investigation Closing to Recall", 'MfrAwarenessToRecall': "Manufacturer Awareness to Recall", 'RecallToOwnerNotification': "Recall to Owner Notification Date"}

Selected_var = st.sidebar.selectbox("Select a process variable", ["First Complaint to Investigation Opening", "Investigation Opening to Closing", "Investigation Closing to Recall", "Manufacturer Awareness to Recall", "Recall to Owner Notification Date"], help = "Select the variable you want to see a visual representation of")
Selected_graph = st.sidebar.selectbox("Select a graph", ["Histogram", "Boxplot"], help = "Select Histogram or Boxplot for numerical variables.")

if Selected_graph == "Histogram":
  for variable, label in Labels.items():
    if label == Selected_var:
      plt = PlotHist(Data[variable], Labels[variable])
  st.pyplot(plt)


else:
  for variable, label in Labels.items():
    if label == Selected_var:
      plt = PlotBox(Data[variable], Labels[variable])
  st.pyplot(plt)
