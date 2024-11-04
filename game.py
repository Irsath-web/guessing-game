import streamlit as st
import random
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
st.title("Guess the Number!")
st.write("I'm thinking of a number between 1 and 100. Can you guess what it is?")
user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.random_number:
        st.write(f"Your guess is too low. Try again!")
    elif user_guess > st.session_state.random_number:
        st.write(f"Your guess is too high. Try again!")
    else:
        st.success(f"Congratulations! You've guessed the number {st.session_state.random_number} in {st.session_state.attempts} attempts!")
        if st.button("Play Again"):
            st.session_state.random_number = random.randint(1, 100)
            st.session_state.attempts = 0
if st.button("Reset Game"):
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.write("The game has been reset! Start guessing again.")
st.write(f"Attempts: {st.session_state.attempts}")


