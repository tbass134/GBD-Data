from dataclasses import dataclass
from json import load
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import boto3
import io

st.set_page_config(layout="wide")
@st.cache
def load_data():
    df = pd.read_csv("GBD-DATA-INPUT-SOURCES-test.csv")
    # df["Age"] = round(df["Age End"] - df["Age Start"] / 365)
    # df = df.drop(["Age Start", "Age End"], axis=1)
    # df = df[df["Location"] != "United States of America" ]

    # fig, ax = plt.subplots()
    # ax  = df.groupby(['Location', 'Risk']).size().unstack()
    # ax.plot(kind='bar', stacked=True)
    # plt.show()
    # st.pyplot()
    # st.write(ax)
    return df




df = load_data()

selected_state = st.selectbox('State', df["Location"].unique())
if selected_state is not None:
    selected_data = df[df["Location"] == selected_state]
    st.write(selected_data)
    st.header("Risks")
    st.bar_chart(selected_data.Risk.value_counts().sort_values(ascending=True))

    st.header("Top 5 Risk Factors")
    st.write(selected_data.Risk.value_counts().sort_values(ascending=False).head(5))

    st.header("Age Distribution")
    st.write(selected_data.Age.value_counts().sort_values(ascending=True))


   


  

    # st.write(selected_data.groupby(['Location', 'Risk']).size().unstack().plot(kind='bar', stacked=True))