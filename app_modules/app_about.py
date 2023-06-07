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
    
    다운로드 : [스마트 치안 빅데이터 : 금융사기] (https://www.bigdata-policing.kr/product/list?vendor_code=all&product_category=&product_type=all&datepicker_type=all&datepicker_from=&datepicker_to=&price_yn=all&orderby=&dateGroup=all&feeGroup=all&dataGruop=all&keyword=%EA%B8%88%EC%9C%B5%EC%82%AC%EA%B8%B0)
    """)
