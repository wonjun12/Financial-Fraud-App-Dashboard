import streamlit as st
import pandas as pd
import numpy as np



from .inputs_date import set_date_st
from .pie_bar_chart import create_pie_chart, create_bar_chart

from .app_damage_module.app_damage_total import run_total_damage_st, run_total_week_st, run_total_opstions_st

def set_weeks(df):
    weeks_list = ['월', '화', '수', '목', '금', '토', '일']
    weeks = df['RGSTN_DT'].dt.dayofweek
    df['weeks'] = weeks.map(lambda x : weeks_list[x])
    df['is_week'] = weeks.map(lambda x: '평일' if x < 5 else '주말')

    return df



def run_damage_func():
    st.title('피해 데이터')

    title_list = ['선택', '전체', '성별', '나이']
    selected_title = st.selectbox('원하시는 기준을 선택하세요!', title_list)

    if selected_title != title_list[0]:
        
        if selected_title == title_list[1]:
            df = pd.read_csv('data/TCH_Gitur.csv')
            opsion_list = df['IBBN'].unique()
        else:
            df = pd.read_csv('data/TCH_Victim.csv')
            df = df.loc[df['IBBN'].str.contains(selected_title)]
            opsion_list = df['IBBN'].unique()

        str_split = lambda x : x[3:]
        str_split_func = np.vectorize(str_split)
        opsion_list = str_split_func(opsion_list) 
            

        selected_opstion = st.radio('종류를 선택하세요!', opsion_list)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

        st.markdown("""---""")

        df_sharch = df.loc[df['IBBN'].str.contains(selected_opstion), ]
        df_sharch['RGSTN_DT'] = pd.to_datetime(df_sharch['RGSTN_DT'])

        start_date, end_date = set_date_st(df_sharch['RGSTN_DT'].min(), df_sharch['RGSTN_DT'].max())
        df_sharch = df_sharch.loc[(df_sharch['RGSTN_DT'] >= start_date) & (df_sharch['RGSTN_DT'] <= end_date), ]

        df_sharch = set_weeks(df_sharch)
        if selected_title != title_list[0]:
            st.subheader(f'{selected_title} 기준 | {selected_opstion} 피해 조회 데이터')

        if selected_title == title_list[1]:
            if selected_opstion == '발생 수':
                run_total_damage_st(df_sharch)
            else :
                run_total_opstions_st(df_sharch, selected_opstion)

                st.markdown("""---""")
                st.subheader('요일별 데이터 확인')
                week_list = {
                    '평일/주말 기준' : 'is_week' , 
                    '요일 기준':'weeks'
                    }
                selected__week = st.selectbox('요일 그룹 확인', week_list.keys())

                run_total_week_st(df_sharch, week_list[selected__week])
            


                # df_values = df_sharch.groupby('TYPE')['DAMAGE'].value_counts().to_frame(name = 'COUNT').reset_index()
                # min_value, max_value = view_size(df_values['DAMAGE'].unique())
                # fig = px.bar(df_values, x='DAMAGE', y='COUNT', color='TYPE', range_x=[min_value, min_value+max_value])
                # fig.update_layout(title = title_str, xaxis=dict(title=''), yaxis=dict(title=''))
                # st.plotly_chart(fig)

            
            
            # df_groups = df_sharch.groupby(week_list[selected__week])
            # selected_week_option = st.selectbox('상세 옵션 선택', df_sharch[week_list[selected__week]].unique())

            # if selected_title == title_list[1]:
            #     df_groups = df_groups['DAMAGE'].value_counts().to_frame(name = 'COUNT').reset_index()
            #     df_groups_value = df_groups.loc[df_groups[week_list[selected__week]] == selected_week_option, ['DAMAGE', 'COUNT']][min_value: min_value+max_value]
            #     min_value, max_value = view_size(df_groups_value)
            #     create_pie_chart(df_groups_value, 'COUNT', df_groups_value['DAMAGE'], f'{selected_week_option} 기준 상위 데이터')
            #     create_bar_chart(df_groups_value, 'COUNT', df_groups_value['DAMAGE'], f'{selected_week_option} 기준 상위 데이터')
            # else:
            #     pass

        st.markdown("""---""")
        st.subheader('참고 데이터 확인')
        if st.checkbox('참고 데이터 프레임 확인하기'):
            st.dataframe(df)
            

            
            
