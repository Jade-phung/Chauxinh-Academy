
import streamlit as st
from random import randint

st.title("Chauxinh Academy 🎮")
st.write("Get 3 correct answers to win. 3 mistakes and game over!")

# Create a new math question
def new_question():
    a = randint(10, 99)
    b = randint(10, 99)
    operation = randint(1, 4)

    if operation == 1:
        symbol = "+"
        answer = a + b
    elif operation == 2:
        symbol = "-"
        answer = a - b
    elif operation == 3:
        symbol = "×"
        answer = a * b
    else:
        symbol = "÷"
        answer = round(a / b, 2)

    st.session_state.a = a
    st.session_state.b = b
    st.session_state.symbol = symbol
    st.session_state.answer = answer


# Remember game progress
if "started" not in st.session_state:
    st.session_state.started = False

if st.button("Start Game / Restart"):
    st.session_state.started = True
    st.session_state.correct = 0
    st.session_state.incorrect = 0
    st.session_state.question = 1
    st.session_state.feedback = ""
    new_question()
    st.rerun()


if st.session_state.started:

    correct = st.session_state.correct
    incorrect = st.session_state.incorrect
    col1, col2 = st.columns(2)
    with col1:
         st.metric("✅ Correct", f"{correct}/3")
    with col2:
        st.metric("❌ Incorrect", f"{incorrect}/3")

    if st.session_state.feedback:
        st.info(st.session_state.feedback)

    if correct >= 3:
        st.success("🎉 Congratulations! You mastered math!")

    elif incorrect >= 3:
        st.error("Game Over! You should review more.")

    else:
        a = st.session_state.a
        b = st.session_state.b
        symbol = st.session_state.symbol

        st.subheader(f"Question {st.session_state.question}")
        st.header(f"{a} {symbol} {b} = ?")

        with st.form(f"question_{st.session_state.question}"):
            user_input = st.text_input(
                "Your answer (round division to 2 decimals):"
            )
            submitted = st.form_submit_button("Submit Answer")

        if submitted:
            try:
                x = float(user_input)
                answer = st.session_state.answer

                if x == answer:
                    st.session_state.correct += 1
                    st.session_state.feedback = "✅ Correct!"
                else:
                    st.session_state.incorrect += 1
                    st.session_state.feedback = (
                        f"❌ Incorrect! The expected answer is {answer}"
                    )

                st.session_state.question += 1

                if (st.session_state.correct < 3
                        and st.session_state.incorrect < 3):
                    new_question()

                st.rerun()

            except ValueError:
                st.warning("Please enter a valid number!")



st.markdown("""
<style>

/* NỀN WEBSITE */
.stApp {
    background-color: #FFF5FA;
}

/* FONT VÀ MÀU CHỮ */
html, body, [class*="st-"] {
    font-family: 'Trebuchet MS', sans-serif;
    color: #342638;
}

/* TIÊU ĐỀ */
h1 {
    color: #C2185B !important;
    font-size: 48px !important;
}

/* NÚT BẤM */
.stButton button,
.stFormSubmitButton button {
    background-color: #FF93CD;
    color: white;
    border-radius: 20px;
    border: none;
    font-weight: bold;
}

/* MÀU NỀN Ô NHẬP */
div[data-baseweb="input"] {
    background-color: 
	#FF93CD !important;
    border: 1px solid #BA9BE8;
    border-radius: 12px;
}

/* MÀU CHỮ KHI NHẬP */
div[data-baseweb="input"] input {
    background-color: transparent !important;
    color: #43215C !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background-color: #FFF7FB;
}

html, body, [class*="st-"] {
    font-family: 'Trebuchet MS', sans-serif;
    color: #39294C;
}

h1 {
    color: #D63384 !important;
}



/* ô metric */
[data-testid="stMetric"] {
    background-color: #FFE4F1;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    border: 2px solid #F8BBD0;
}
</style>
""", unsafe_allow_html=True)