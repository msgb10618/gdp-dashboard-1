import streamlit as st

# 웹 페이지 제목
st.title("🍿 영화관 세트메뉴 조합")

popcorn_options = ["기본", "어니언", "카라멜"]
drink_options = ["생수", "탄산음료"]

st.subheader("모든 세트메뉴 리스트")

# 중첩 반복문을 돌며 화면에 출력
for popcorn in popcorn_options:
    for drink in drink_options:
        # st.write()를 사용해 웹 화면에 텍스트 출력
        st.write(f"🎬 **세트메뉴:** {popcorn} 팝콘 + {drink}")