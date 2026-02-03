import streamlit as st
import random
from quiz_data import quiz_list


# ===== セッション初期化 =====
if "quiz" not in st.session_state:
    st.session_state.used_quizzes = []
    st.session_state.quiz = random.choice(quiz_list)
    st.session_state.used_quizzes.append(st.session_state.quiz)
    st.session_state.answered = False
    st.session_state.correct_count = 0
    st.session_state.total_answered = 0

# ===== session_state 初期化 =====
if "total_answered" not in st.session_state:
    st.session_state.total_answered = 0

if "correct_count" not in st.session_state:
    st.session_state.correct_count = 0

if "used_quizzes" not in st.session_state:
    st.session_state.used_quizzes = []

if "quiz" not in st.session_state:
    st.session_state.quiz = random.choice(quiz_list)
    st.session_state.used_quizzes.append(st.session_state.quiz)
    st.session_state.answered = False



quiz = st.session_state.quiz
# ===== 選択肢シャッフル（キーは固定）=====
if "shuffled_choices" not in st.session_state:
    keys = list(quiz["choices"].keys())          # ["a", "b", "c", "d"]
    values = list(quiz["choices"].values())      # 選択肢文
    random.shuffle(values)

    st.session_state.shuffled_choices = dict(zip(keys, values))



# ===== 画面表示 =====
st.title("🔥 消防設備士 過去問道場")

if st.session_state.total_answered > 0:
    rate = st.session_state.correct_count / st.session_state.total_answered
    st.write(f"### 正答率：{rate:.1%} ({st.session_state.correct_count}/{st.session_state.total_answered})")
progress = len(st.session_state.used_quizzes) / len(quiz_list)
st.progress(progress)
st.write(f"{len(st.session_state.used_quizzes)} / {len(quiz_list)} 問")


st.write("### 問題")
st.write(quiz["question"])

choice = st.radio(
    "選択肢を選んでください",
    list(st.session_state.shuffled_choices.keys()),
    format_func=lambda x: f"{x}：{st.session_state.shuffled_choices[x]}"
)

# ===== 解答ボタン =====
if not st.session_state.answered:
    if st.button("解答する"):
        st.session_state.answered = True
        st.session_state.total_answered += 1

        if choice == quiz["answer"]:
            st.session_state.correct_count += 1

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
            # 次の問題へ
            keys = list(next_quiz["choices"].keys())
            values = list(next_quiz["choices"].values())
            random.shuffle(values)
            st.session_state.shuffled_choices = dict(zip(keys, values))

            st.rerun()
        else:
            st.success("🎉 全ての問題を解き終わりました！")



















