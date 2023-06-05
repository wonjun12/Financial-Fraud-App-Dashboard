import streamlit as st
import pandas as pd

from .inputs_date import set_date_st
from .pie_bar_chart import create_pie_chart, create_bar_chart

def run_suspect_phone():
    st.title('용의자 통신사 데이터 확인')
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
    st.subheader('참고 데이터 확인')
    if st.checkbox('참고 데이터 프레임 확인하기'):
        st.dataframe(df)
