import streamlit as st
import pandas as pd
import numpy as np

from .inputs_date import set_date_st

from .app_damage_module.app_damage_total import run_total_damage_st, run_total_week_st, run_total_opstions_st
from .app_damage_module.app_damage_sex import run_sex_st, run_sex_opstions_st
from .app_damage_module.app_damage_age import run_age_st, run_age_opstions_st

def select_week():
    st.markdown("""---""")
    st.subheader('요일별 데이터 확인')
    week_list = {
        '평일/주말 기준' : 'is_week' , 
        '요일 기준':'weeks'
        }
    selected__week = st.selectbox('요일 그룹 확인', week_list.keys())

    return week_list[selected__week]

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

        df_sharch = df.loc[df['IBBN'].str.contains(selected_opstion), ].copy()
        df_sharch['RGSTN_DT'] = pd.to_datetime(df_sharch['RGSTN_DT'])

        start_date, end_date = set_date_st(df_sharch['RGSTN_DT'].min(), df_sharch['RGSTN_DT'].max())
        df_sharch_copy = df_sharch.loc[(df_sharch['RGSTN_DT'] >= start_date) & (df_sharch['RGSTN_DT'] <= end_date), ]

        if selected_title != title_list[0]:
            st.subheader(f'{selected_title} 기준 | {selected_opstion} 피해 조회 데이터')

        if selected_title == title_list[1]:
            if selected_opstion == '발생 수':
                run_total_damage_st(df_sharch_copy)
            else :
                run_total_opstions_st(df_sharch, selected_opstion)
                week = select_week()
                run_total_week_st(df_sharch_copy, week)
        elif selected_title == title_list[2]:
            run_sex_st(df_sharch_copy)
            week = select_week()
            run_sex_opstions_st(df_sharch_copy, week)
        elif selected_title == title_list[3]:
            run_age_st(df_sharch_copy)
            week = select_week()
            run_age_opstions_st(df_sharch_copy, week)


        st.markdown("""---""")
        st.subheader('참고 데이터 확인')
        if st.checkbox('참고 데이터 프레임 확인하기'):
            st.dataframe(df)
            

            
            
