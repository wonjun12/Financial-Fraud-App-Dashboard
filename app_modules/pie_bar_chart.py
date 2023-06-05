import streamlit as st

import plotly.express as px
import matplotlib.pyplot as plt

def create_pie_chart(data, values, names, titles):
    fig = px.pie(data,values=values,names=names, title=titles)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)

def create_bar_chart(data,y, x,  titles):
    fig = px.bar(data, x=x, y=y)
    fig.update_layout(title = titles, xaxis=dict(title=''), yaxis=dict(title=''))
    st.plotly_chart(fig)
