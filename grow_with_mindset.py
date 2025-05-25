import streamlit as st
import datetime
import random

# Load motivational quotes from a file
def load_quotes():
    with open("quotes.txt", "r", encoding="utf-8") as file:
        return [quote.strip() for quote in file.readlines() if quote.strip()]

# Introduction section
def show_intro():
    st.title("🌱 Grow With Mindset")
    st.markdown("""
    Welcome to **Grow With Mindset**, an interactive app that helps you practice and build a growth mindset.

    **What’s a Growth Mindset?**  
    A growth mindset is the belief that your abilities can be developed through dedication and hard work. This view creates a love for learning and resilience.

    Use the menu to explore and practice!
    """)

# Reflection tracker
def daily_reflection():
    st.header("📝 Daily Reflection")

    today = str(datetime.date.today())
    reflections = st.session_state.get("reflections", {})
    prev_entry = reflections.get(today)

    st.markdown(f"### Today: {today}")
    answer = st.text_area("What challenge did you face today and how did you respond?", value=prev_entry or "")

    if st.button("Save Reflection"):
        reflections[today] = answer
        st.session_state["reflections"] = reflections
        st.success("Reflection saved!")

    if reflections:
        st.markdown("### 📅 Previous Reflections")
        for date, text in sorted(reflections.items(), reverse=True):
            st.markdown(f"**{date}**: {text}")

# Quiz section
def growth_mindset_quiz():
    st.header("🧠 Mindset Quiz")
    st.write("Identify whether the following statements are a **Growth Mindset** or **Fixed Mindset**.")

    questions = {
        "I avoid challenges to not look stupid.": "Fixed",
        "I can always improve if I work hard.": "Growth",
        "Feedback is criticism.": "Fixed",
        "Mistakes help me learn.": "Growth",
        "My intelligence is fixed.": "Fixed",
        "Effort leads to mastery.": "Growth"
    }

    score = 0
    for q, correct in questions.items():
        answer = st.radio(q, ["Growth", "Fixed"], key=q)
        if answer == correct:
            score += 1

    if st.button("Check Score"):
        st.success(f"You got {score} out of {len(questions)} correct!")
        if score == len(questions):
            st.balloons()

# Quote of the day
def show_quote(quotes):
    st.header("💬 Quote of the Day")
    st.info(random.choice(quotes))

# Feedback journal
def feedback_journal():
    st.header("🗒️ Feedback Journal")
    journal = st.text_area("Write down any feedback or lesson you learned recently:")
    if st.button("Save Journal Entry"):
        st.success("Journal saved (session-only for now).")
        st.session_state["journal"] = journal

# Sidebar menu
def main():
    st.sidebar.title("📚 Navigation")
    menu = ["Home", "Daily Reflection", "Mindset Quiz", "Quote", "Feedback Journal"]
    choice = st.sidebar.radio("Go to:", menu)

    quotes = load_quotes()

    if choice == "Home":
        show_intro()
    elif choice == "Daily Reflection":
        daily_reflection()
    elif choice == "Mindset Quiz":
        growth_mindset_quiz()
    elif choice == "Quote":
        show_quote(quotes)
    elif choice == "Feedback Journal":
        feedback_journal()

if __name__ == "__main__":
    main()
