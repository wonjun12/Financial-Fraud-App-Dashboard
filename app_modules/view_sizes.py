import streamlit as st

def view_size(df, n):
    min_text, max_test = st.columns([1,1])
    with min_text:
        min_value = st.slider(f'보여줄 상위 최소 기준 {n}', min_value=0, max_value=df.shape[0])
    with max_test:
        max_value = st.slider(f'보여줄 최대 갯수 {n}', min_value=1, value=10, max_value=15)
    return min_value, max_value