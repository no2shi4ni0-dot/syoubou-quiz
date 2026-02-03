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
if "shuffled_items" not in st.session_state:
    items = list(quiz["choices"].items())  # [('a','文章'),...]
    random.shuffle(items)
    st.session_state.shuffled_items = items




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

maru = ["①", "②", "③", "④", "⑤"]

labels = {
    i: f"{maru[i]}：{text}"
    for i, (_, text) in enumerate(st.session_state.shuffled_items)
}


selected_index = st.radio(
    "選択肢を選んでください",
    options=list(labels.keys()),
    format_func=lambda x: labels[x]
)


# ===== 解答ボタン =====
if not st.session_state.answered:
    if st.button("解答する"):
        st.session_state.answered = True
        st.session_state.total_answered += 1

        selected_key = st.session_state.shuffled_items[selected_index][0]

        if selected_key == quiz["answer"]:
            st.session_state.correct_count += 1


# ===== 結果表示 =====
if st.session_state.answered:
    selected_key = st.session_state.shuffled_items[selected_index][0]

    if selected_key == quiz["answer"]:
        st.success("⭕ 正解！")
    else:
        # 正解キーが何番目か探す
        correct_index = next(
            i for i, (key, _) in enumerate(st.session_state.shuffled_items)
            if key == quiz["answer"]
        )
        st.error(f"❌ 不正解（正解：{maru[correct_index]}）")

    st.write("### 解説")
    st.write(quiz["explanation"])

if st.session_state.answered:
    if st.button("次の問題へ"):
        remaining = [
            q for q in quiz_list if q not in st.session_state.used_quizzes
        ]

        if remaining:
            next_quiz = random.choice(remaining)
            st.session_state.quiz = next_quiz
            st.session_state.used_quizzes.append(next_quiz)
            st.session_state.answered = False

            items = list(next_quiz["choices"].items())
            random.shuffle(items)
            st.session_state.shuffled_items = items

            st.rerun()
        else:
            st.success("🎉 全問終了！")






















