import streamlit as st

import plotly.express as px

from ..view_sizes import view_size


def run_sex_st(df):
    df_values = df.groupby(['TYPE', 'DAMAGE'])['COUNT'].sum().sort_values(ascending=False).to_frame().reset_index()

    min_value, max_value = view_size(df_values['DAMAGE'].unique(), 1)

    fig = px.bar(df_values, x='DAMAGE', y='COUNT', color='TYPE', range_x=[min_value, min_value+max_value])
    fig.update_layout(xaxis=dict(title=''), yaxis=dict(title=''))
    st.plotly_chart(fig)

def run_sex_opstions_st(df, week):
    
   
    selected_week_option = st.selectbox('상세 옵션 선택', df[week].unique())
    df_groups = df.loc[df[week] == selected_week_option, ['TYPE', 'DAMAGE', 'COUNT']]
    df_groups_value = df_groups.groupby(['TYPE','DAMAGE'])['COUNT'].sum().sort_values(ascending=False).to_frame().reset_index()

    min_value, max_value = view_size(df_groups_value, 2)

    fig = px.bar(df_groups_value, x='DAMAGE', y='COUNT', color='TYPE', range_x=[min_value, min_value+max_value])
    fig.update_layout(xaxis=dict(title=''), yaxis=dict(title=''))
    st.plotly_chart(fig)