import streamlit as st

st.title('🍔Welcome to Burger world!🍔')
st.header('안녕하세요 저는 우주 최강 햄버거입니다.')
st.subheader('햄버거에 대해 얼마나 아시나요?')

my_site = st.text_input('당신도 햄버거가 되고 싶나요?')  # input 값을 활용하기 위해선 변수에 담아줘야함
print(my_site)      
st.write(my_site)

if st.button(f'{my_site} 버거월드 접속하기'):
    st.success(f"{my_site} 버거월드에 접속중🍔", icon='✅')

