import streamlit as st

st.title('버거월드가 마음에 드셨다면 좋아요를 눌러주세요👍')

if "버거월드가 마음에 드셨다면 좋아요를 눌러주세요👍" not in st.session_state:
    st.session_state.like_count = 0

if st.button('🍔👍'):
    st.session_state.like_count += 1

if st.button('초기화!'):
    like_count = 0

st.write(f'누적된 좋아요 수: {st.session_state.like_count}')


# import streamlit as st

# st.title('Counter')

# if "customer_count" not in st.session_state:
#     st.session_state.customer_count = 0

# if st.button('손님 한 명 추가요~'):
#     st.session_state.customer_count += 1

# if st.button('오늘 장사 끝! 손님 수 초기화!'):
#     customer_count = 0

# st.write(f'지금까지 온 손님 수: {st.session_state.customer_count}')