import streamlit as st
from streamlit_option_menu import option_menu

from app_modules.app_about import run_about_func
from app_modules.app_suspect_phone import run_suspect_phone
from app_modules.app_resion import run_resion_func
from app_modules.app_damage import run_damage_func

def main():
    with st.sidebar:
        st.image('image/side_image.png')
        select_list = ['About', '통신사 데이터', '지역 데이터', '피해 데이터']
        selected = option_menu('메뉴', select_list, icons=['house', 'bi-arrow-return-right', 'bi-arrow-return-right', 'bi-arrow-return-right'], menu_icon='cast')

    if selected == select_list[0]:
        run_about_func()
    elif selected == select_list[1]:
        run_suspect_phone()
    elif selected == select_list[2]:
        run_resion_func()
    else:
        run_damage_func()
        


if __name__ == '__main__':
    main()
