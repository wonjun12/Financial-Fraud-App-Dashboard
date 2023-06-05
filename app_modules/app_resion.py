import streamlit as st
import pandas as pd

from .inputs_date import set_date_st
from .pie_bar_chart import create_pie_chart, create_bar_chart
def view_chart(df):
    start_date, end_date = set_date_st(df['RGSTN_DT'].min(), df['RGSTN_DT'].max())

    df_shrch = df.loc[(df['RGSTN_DT'] >= start_date) & (df['RGSTN_DT'] <= end_date), ]

    st.subheader('시도 기준')
    
    df_wdar = df_shrch.value_counts('WDAR_CTPR_NM').to_frame(name='COUNT')

    set_size = st.slider('보여줄 기준점을 정해주세요!', min_value=0, max_value=df_wdar.shape[0]-10)
    create_pie_chart(df_wdar[set_size:set_size+10], 'COUNT', df_wdar[set_size:set_size+10].index, '시도 그래프')
    create_bar_chart(df_wdar[set_size:set_size+10],'COUNT', df_wdar[set_size:set_size+10].index,  '시도 그래프')

    st.markdown("""---""")
    st.subheader('시군구 기준')

    wdar_list = df_wdar.index
    selected_wdar = st.selectbox('원하시는 기준점을 선택하세요!', wdar_list)
    df_legal = df_shrch.loc[df_shrch['WDAR_CTPR_NM'] == selected_wdar, 'LEGAL_SIGUNGU_NM'].value_counts().to_frame(name = 'COUNT')
    create_pie_chart(df_legal, 'COUNT', df_legal.index, '시군구 그래프')
    create_bar_chart(df_legal,'COUNT', df_legal.index,  '시군구 그래프')


def run_resion_func():
    st.title('용의자 및 피해자의 지역 확인')
    st.markdown("""---""")
#
    df = pd.read_csv('data/TCH_Resion.csv')
    df['RGSTN_DT'] = pd.to_datetime(df['RGSTN_DT'])
    
    

    st.markdown("#### 구분 선택")

    select_list = ['선택', '용의자 지역', '피해자 지역']
    selected_box = st.selectbox('원하는 그룹을 선택하세요!', select_list)
    st.markdown("""---""")

    if selected_box != select_list[0]:
        view_chart(df.loc[df['IBBN'] == selected_box[:3], ])

        st.markdown("""---""")
        st.subheader('참고 데이터 확인')
        if st.checkbox('참고 데이터 프레임 확인하기'):
            st.dataframe(df)
    
