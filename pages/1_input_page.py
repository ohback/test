import streamlit as st

st.title('버거월드 입장하기🍔')
 
nickname = st.text_input("닉네임 입력")
how_many = st.number_input("햄최몇? (5개 미만 입장불가)", min_value=5)

r_options = ["버거킹", "맥도날드", "롯데리아", "맘스터치", "파이브가이즈"]
choice = st.radio("좋아하는 햄버거 가게를 선택해주세요", r_options)
r_options2 = ["빅맥", "상하이스파이시", "베이컨토마토디럭스", "불고기버거", "슈슈버거", "와퍼", "치즈와퍼", "치즈버거", "치킨버거"]
selected_many = st.multiselect("좋아하는 햄버거를 선택해주세요(중복 가능)", r_options2)

checked = st.checkbox("버거월드에 정보 제공 동의")
if checked == True:
    st.write('버거월드로 떠날 준비 완료!🏃‍➡️🏃‍♀️‍➡️🏃‍♂️‍➡️')


if st.button('버거월드 입장!'):
    st.write(f'이름: {nickname}')
    st.write(f'햄최몇: {how_many}')
    st.write(f'좋아하는 햄버거 가게: {choice}')
    st.write(f'좋아하는 햄버거: {selected_many}')
    st.write(f'개인정보 제공 동의: {checked}')