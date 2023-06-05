import streamlit as st
import pandas as pd

def set_date_st(mins, maxs):
    start_date, end_date = st.columns([1,1])

    with start_date:
        st.subheader('조회 시작 날짜')
        start = st.date_input('검색할 시작 날짜를 선택하세요!', min_value=mins.date(), max_value=maxs.date(), value=mins.date())
    with end_date:
        st.subheader('조회 마지막 날짜')
        end = st.date_input('검색할 마지막 날짜를 선택하세요!', min_value=mins.date(), max_value=maxs.date(), value=maxs.date())
    st.markdown("""---""")
    return pd.to_datetime(start), pd.to_datetime(end)