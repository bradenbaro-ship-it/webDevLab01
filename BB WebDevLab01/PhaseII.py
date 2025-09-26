import streamlit as st

st.set_page_config(page_title="Fahrenheit 451 Quiz")

st.title("Fahrenheit 451 — Which Character Do You Think Like?")
st.write(
    "Answer these questions inspired by Ray Bradbury's *Fahrenheit 451*. "
    "At the end, you’ll see which character your mindset resembles."
)

st.image("images/f451_cover.jpg", caption="Fahrenheit 451")

q1 = st.radio(
    "1) At the start, Montag burns books as part of his job. How do you respond to that?",
    ["It's just a job, he doesn’t know better.",
     "It’s horrifying — knowledge should be preserved.",
     "It makes me curious why society allowed this."]
)

q2 = st.multiselect(
    "2) Which themes from the novel stood out most?",
    ["Censorship", "Conformity vs. Individuality", "Technology’s role in society", "Knowledge vs. Ignorance"]
)

st.image("images/f451_fire.jpg", caption="The power and danger of fire")

q3 = st.slider(
    "3) On a scale of 1–10, how strongly do you agree with Clarisse that asking questions is more important than giving answers?",
    1, 10, 5
)

q4 = st.number_input(
    "4) How many books have you actually read cover-to-cover in the last year?",
    min_value=0, max_value=100, value=5
)

st.image("images/f451_books.jpg", caption="Books as symbols of resistance")

q5 = st.text_input(
    "5) In one word, describe how you felt at the end of the novel:"
)
if st.button("See My Result"):
    score = 0
    if q1 == "It’s horrifying — knowledge should be preserved.":
        score += 3
    elif q1 == "It makes me curious why society allowed this.":
        score += 2
    else:
        score += 1

    if "Censorship" in q2:
        score += 2
    if "Technology’s role in society" in q2:
        score += 1
    if "Knowledge vs. Ignorance" in q2:
        score += 2

    score += q3 // 3
    score += min(q4, 10) // 2

    if score >= 9:
        result = "You’re most like Clarisse — curious, thoughtful, and questioning."
    elif 6 <= score < 9:
        result = "You’re most like Montag — conflicted but searching for truth."
    else:
        result = "You’re most like Mildred — shaped by society, but still human underneath."

    st.subheader("Your Result")
    st.write(result)
    if q5:
        st.write(f"You summed up your feelings with the word: **{q5}**")

    st.metric("Quiz Score", score)
    st.progress(min(score, 10))
    st.balloons()

