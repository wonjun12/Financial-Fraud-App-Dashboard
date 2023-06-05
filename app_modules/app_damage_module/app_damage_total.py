import streamlit as st
import pandas as pd

import plotly.express as px

from ..view_sizes import view_size
from ..pie_bar_chart import create_pie_chart, create_bar_chart

def run_total_damage_st(df):
    df['DAMAGE'] = pd.to_numeric(df['DAMAGE'])
    fig = px.line(df, x = 'RGSTN_DT', y = 'DAMAGE', title='날짜에 따른 피해 발생 수')
    fig.update_layout(xaxis=dict(title=''), yaxis=dict(title=''))
    st.plotly_chart(fig)
    
    st.markdown("""---""")
    st.subheader('요일별 데이터 확인')
    week_list = ['평일/주말 기준' , '요일 기준']
    selected__week = st.selectbox('요일 그룹 확인', week_list)
    if selected__week == week_list[0]:
        fig_week = px.line(df, x = 'RGSTN_DT', y = 'DAMAGE', color='is_week', title='평일/주말 그래프')
        fig_week.update_layout(xaxis=dict(title=''), yaxis=dict(title=''))
        st.plotly_chart(fig_week)

        is_week_group = df.groupby('is_week')['DAMAGE'].sum().to_frame()
        is_week_group['DAMAGE'][0] //= 2
        is_week_group['DAMAGE'][1] //= 5
        create_pie_chart(is_week_group, 'DAMAGE', is_week_group.index, '평일/주말 평균 그래프')

    else :
        fig_week = px.line(df, x = 'RGSTN_DT', y = 'DAMAGE', color='weeks', title='요일별 그래프')
        fig_week.update_layout(xaxis=dict(title=''), yaxis=dict(title=''))
        st.plotly_chart(fig_week)

        weeks_group = df.groupby('weeks')['DAMAGE'].sum().to_frame()
        create_pie_chart(weeks_group, 'DAMAGE', weeks_group.index, '요일별 그래프')

def run_total_opstions_st(df, opstions):
    title_str = f'{opstions} 데이터'

    df_values = df['DAMAGE'].value_counts().to_frame(name = 'COUNT')
    min_value, max_value = view_size(df_values, 1)
    create_pie_chart(df_values[min_value:min_value+max_value], 'COUNT', df_values[min_value:min_value+max_value].index, title_str)
    create_bar_chart(df_values[min_value:min_value+max_value], 'COUNT', df_values[min_value:min_value+max_value].index, title_str)


def run_total_week_st(df, week):
    df_groups = df.groupby(week)['DAMAGE'].value_counts().to_frame(name = 'COUNT').reset_index()
    selected_week_option = st.selectbox('상세 옵션 선택', df[week].unique())

    df_groups_value = df_groups.loc[df_groups[week] == selected_week_option, ['DAMAGE', 'COUNT']].reset_index(drop=True)
    min_value, max_value = view_size(df_groups_value, 2)
    
    df_groups_value = df_groups_value.iloc[min_value: min_value+max_value, ]
    
    
    create_pie_chart(df_groups_value, 'COUNT', df_groups_value['DAMAGE'], f'{selected_week_option} 기준 상위 데이터')
    create_bar_chart(df_groups_value, 'COUNT', df_groups_value['DAMAGE'], f'{selected_week_option} 기준 상위 데이터')