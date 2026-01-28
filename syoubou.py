import streamlit as st
import random

# ===== 問題データ（ここを自由に編集） =====
quiz_list = [
    {
        "question": "自動火災報知設備において、階段の警戒区域の扱いとして正しいものはどれか。",
        "choices": {
            "a": "各階ごとに警戒区域とする",
            "b": "居室と同一警戒区域に含める",
            "c": "縦に連続する1警戒区域として扱う",
            "d": "警戒区域に含めない"
        },
        "answer": "c",
        "explanation": "階段は縦に連続した空間であるため、原則として1つの警戒区域として扱う。"
    },
    {
        "question": "P型2級受信機で扱える警戒区域数として適切なものはどれか。",
        "choices": {
            "a": "3区域",
            "b": "5区域",
            "c": "8区域",
            "d": "10区域"
        },
        "answer": "b",
        "explanation": "P型2級受信機は最大5回線（5警戒区域）まで対応可能である。"
    }
]

# ===== セッション初期化 =====
if "quiz" not in st.session_state:
    st.session_state.quiz = random.choice(quiz_list)
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
        st.session_state.quiz = random.choice(
            [q for q in quiz_list if q != st.session_state.quiz]
        )
        st.session_state.answered = False
        st.rerun()

    






