import streamlit as st
import pandas as pd


st.title('프랜차이즈별 점포 증가 추이')

data = pd.DataFrame({
    "브랜드": ["버거킹", "맥도날드", "롯데리아", "맘스터치", "파이브가이즈"],
    "매장수": [100, 150, 200, 50, 30],
    "증가율(%)": [10, 20, 30, -5, 80],
    "인지도(%)": [80, 90, 95, 50, 35]
})


st.dataframe(data, use_container_width=80)

# # edited_data = st.data_editor(data)
# # st.write(edited_data)

bar_data = data.set_index('브랜드')[['매장수', '증가율(%)', '인지도(%)']]
st.bar_chart(bar_data)



# data2 = pd.DataFrame({
#     "-": ["2020", "2021", "2022", "2023", "2024"],
#     "버거킹": [120, 35, 20],
#     "맥도날드": [100, 50, 30],
#     "롯데리아": [150, 40, 60],
#     "맘스터치": [50, 20, 32],
#     "파이브가이즈": [25, 20, 30]
# })



line_data = data.set_index('브랜드')[['매장수', '증가율(%)', '인지도(%)']]
st.line_chart(line_data)

fig = data.plot.pie(
    y="인지도(%)",
    labels=data["브랜드"],
    autopct="%1.1f%%",
    figsize=(6, 6),
    legend=False,
    title="브랜드별 점포 증가율"
).get_figure()
st.pyplot(fig)





# st.title('프랜차이즈별 점포 증가 추이')


# data = pd.DataFrame({
#     "-": ["매장수", "증가율(%)", "인지도(%)"],
#     "버거킹": [120, 35, 20],
#     "맥도날드": [100, 50, 30],
#     "롯데리아": [150, 40, 60],
#     "맘스터치": [50, 20, 32],
#     "파이브가이즈": [25, 20, 30]
# })

# st.dataframe(data, use_container_width=80)

# # st.bar_chart(data.set_index('브랜드')['매장수'])
# line_data = data.set_index('-')[['버거킹', '맥도날드', '롯데리아', '맘스터치', '파이브가이즈']]
# st.line_chart(line_data)

# fig = data.plot.pie(
#     y="인지도(%)",
#     labels=data["브랜드"],
#     autopct="%1.1f%%",
#     figsize=(6, 6),
#     legend=False,
#     title="브랜드별 점포 증가율"
# ).get_figure()
# st.pyplot(fig)