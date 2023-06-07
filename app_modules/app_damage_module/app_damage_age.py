import streamlit as st

import plotly.express as px

from ..view_sizes import view_size

def run_age_st(df):
    selected_years = st.multiselect('보시고 싶은 년대생 기준을 추가하세요!', df['TYPE'].unique(), default=df['TYPE'].unique()[:2])
    df_values = df.loc[df['TYPE'].map(lambda x : True if x in selected_years else False), ]

    df_values = df_values.groupby(['TYPE', 'DAMAGE'])['COUNT'].sum().sort_values(ascending=False).to_frame().reset_index()

    min_value, max_value = view_size(df_values['DAMAGE'].unique(), 1)
    
    fig = px.bar(df_values, x='DAMAGE', y='COUNT', color='TYPE', range_x=[min_value, min_value+max_value])
    fig.update_layout(title = '년대생 기준',xaxis=dict(title=''), yaxis=dict(title=''))
    st.plotly_chart(fig)

def run_age_opstions_st(df, week):
    selected_years = st.multiselect('보시고 싶은 년대생 기준을 추가하세요!!', df['TYPE'].unique(), default=df['TYPE'].unique()[:2])
    df_values = df.loc[df['TYPE'].map(lambda x : True if x in selected_years else False), ]

    selected_week_option = st.selectbox('상세 옵션 선택', df_values[week].unique())
    df_groups = df_values.loc[df[week] == selected_week_option, ['TYPE', 'DAMAGE', 'COUNT']]

    df_groups_value = df_groups.groupby(['TYPE', 'DAMAGE'])['COUNT'].sum().sort_values(ascending=False).to_frame().reset_index()
    
    min_value, max_value = view_size(df_values['DAMAGE'].unique(), 2)

    fig = px.bar(df_groups_value, x='DAMAGE', y='COUNT', color='TYPE', range_x=[min_value, min_value+max_value])
    fig.update_layout(title = '년대생 기준.',xaxis=dict(title=''), yaxis=dict(title=''))
    st.plotly_chart(fig)
    