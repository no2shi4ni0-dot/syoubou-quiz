import streamlit as st
import random
from quiz_data import quiz_list


# ===== セッション初期化 =====
if "quiz" not in st.session_state:
    st.session_state.used_quizzes = []
    st.session_state.quiz = random.choice(quiz_list)
    st.session_state.used_quizzes.append(st.session_state.quiz)
    st.session_state.answered = False


quiz = st.session_state.quiz

# ===== 画面表示 =====
st.title("🔥 消防設備士 過去問道場")

st.write("### 問題")
st.write(quiz["question"])

choice = st.radio(
    "選択肢を選んでください",
    list(quiz["choices"].keys()),
    format_func=lambda x: f"{x}：{quiz['choices'][x]}"
)

# ===== 解答ボタン =====
if st.button("解答する"):
    st.session_state.answered = True
 
# ===== 結果表示 =====
if st.session_state.answered:
    if choice == quiz["answer"]:
        st.success("⭕ 正解！")
    else:
        st.error(f"❌ 不正解（正解：{quiz['answer']}）")

    st.write("### 解説")
    st.write(quiz["explanation"])
    if st.button("次の問題へ"):
    remaining_quizzes = [
        q for q in quiz_list if q not in st.session_state.used_quizzes
    ]

    if remaining_quizzes:
        next_quiz = random.choice(remaining_quizzes)
        st.session_state.quiz = next_quiz
        st.session_state.used_quizzes.append(next_quiz)
        st.session_state.answered = False
        st.rerun()
    else:
        st.success("🎉 全ての問題を解き終わりました！")


    










