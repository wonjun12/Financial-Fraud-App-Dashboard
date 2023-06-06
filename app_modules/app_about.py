import streamlit as st

def run_about_func():
    
    st.image('image/about.png')

    st.title('금융사기 정보 데이터 확인')
    
    st.write('금융사기에 대해 용의자와 피해자에 따른 정보를 확인 하실 수 있습니다!')

    st.markdown("""
    - 용의자 통신사 데이터
    - 용의자 및 피해자 지역 데이터
    - 피해자 피해 데이터
       - 피해자 전체 데이터
       - 피해자 성별 기준 데이터
       - 피해자 나이 기준 데이터
    
    [다운로드 링크] [http]()
    """)
