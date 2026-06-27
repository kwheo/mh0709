import streamlit as st

st.title("나의 첫 번째 웹앱")

st.write("VSCode, uv, Streamlit을 이용해서 만든 웹앱입니다.")

name = st.text_input("이름을 입력하세요")

if name:
    st.success(f"{name}님, 반갑습니다!")

age = st.slider("나이를 선택하세요", 0, 100, 0)

st.write(f"선택한 나이는 {age}세입니다.")

st.header("관심 분야 선택")
interest = st.selectbox(
    "관심 있는 분야를 선택하세요",
    ["인공지능", "데이터분석", "웹앱 개발", "디지털 리터러시"]
)
st.write(f"선택한 관심 분야는 {interest}입니다.")