import streamlit as st
import pandas as pd

from .inputs_date import set_date_st
from .pie_bar_chart import create_pie_chart, create_bar_chart

def run_suspect_phone():
    st.title('용의자 통신사 데이터 확인')
    st.markdown("""
        - 가장 많이 사용된 통신사 데이터에 대한 신뢰도를 얻어,
        - 가장 사용이 많이 안된 통신사들에 대한 정보를 얻기 위한 데이터 입니다.
        - 이를 통해 생각지도 못한 통신사로 인해 사기를 당하는 경우가 발생하는 것을 알 수 있습니다.""")
    st.markdown("""---""")

    df = pd.read_csv('data/TCH_Suspect_Phone.csv')
    df['RGSTN_DT'] = pd.to_datetime(df['RGSTN_DT'])

    start_date, end_date = set_date_st(df['RGSTN_DT'].min(), df['RGSTN_DT'].max())

    df_shrch = df.loc[(df['RGSTN_DT'] >= start_date) & (df['RGSTN_DT'] <= end_date), ]
    

    chart_data = df_shrch.value_counts('RSRC_INTNT_SRVIC_OFR').to_frame(name='COUNT')

    st.subheader('많이 사용된 용의자 통신사')
    create_pie_chart(chart_data[:10], 'COUNT', chart_data[:10].index, '가장 많이 사용된 통신사 데이터')
    create_bar_chart(chart_data[:10],'COUNT', chart_data.index[:10], '가장 많이 사용된 통신사 데이터')

    st.markdown("""---""")
    
    st.subheader('기타 용의자 통신사')
    st.markdown('#### 범위 선택')
    min_size_inputs, max_size_inputs = st.columns([1,1])
    with min_size_inputs:
        min_size = st.slider('보여줄 상위 최소 기준.', min_value=0, max_value=chart_data.shape[0]-1)
    with max_size_inputs:
        max_size = st.slider('보여줄 최대 갯수.', min_value=1, value=10, max_value=15)
    create_pie_chart(chart_data[min_size:min_size+max_size], 'COUNT', chart_data[min_size:min_size+max_size].index, '기타 통신사 데이터')
    create_bar_chart(chart_data[min_size:min_size+max_size], 'COUNT', chart_data.index[min_size:min_size+max_size], '기타 통신사 데이터')


    st.markdown("""---""")
    st.subheader('데이터 확인')
    if st.checkbox('데이터 프레임 확인하기'):
        st.dataframe(df)
