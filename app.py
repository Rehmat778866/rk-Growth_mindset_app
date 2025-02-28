# Streamlit

import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")


st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to your Growth Journey!")
st.write("The journey to becoming a Full-Stack Developer & AI Engineer is a path of relentless learning, problem-solving, and innovation. It’s about embracing challenges as opportunities, continuously expanding your technical expertise, and developing a growth mindset that fuels success. A true expert doesn’t settle for limits but pushes beyond them—mastering frontend and backend development, understanding databases, cloud computing, and harnessing the power of AI to build intelligent solutions. Each line of code, every bug fixed, and every project completed takes you one step closer to mastery. Stay curious, adaptable, and persistent—because the tech world is ever-evolving, and those who embrace the journey with passion and resilience will shape the future. Keep learning, keep building, and keep growing—your success is inevitable.")

# quote section
st.header("𝐓𝐨𝐝𝐚𝐲's 𝐆𝐫𝐨𝐰𝐭𝐡 𝐌𝐢𝐧𝐝𝐬𝐞𝐭 QUOTE 🚀")
st.write("'Success is not final, failure is not fatal: it is the courage to continue that counts'.- winston churchill")

st.header("What's your challenge today?")
user_input = st.text_input("Describe a challenge you're facing:")

# Condition
if user_input:
    st.success(f" 💪You are facing: {user_input}. keep focus on your goals! ")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflexing
    st.header("Reflect on your Learning💞")
    reflection = st.text_area(" Write your reflections here: ")

if reflection:
    st.success(f" ⭐Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help your grow! Share your struggle")

# acheivements
st.header("🏆Celebrate! You Win 🏆🎉")
achievement = st.text_input("Share something you're recently accomplished:")

if achievement:
    st.success(f"✨𝓐𝓶𝓪𝔃𝓲𝓷𝓰! 𝓨𝓸𝓾 𝓐𝓬𝓱𝓲𝓮𝓿𝓮𝓭! {achievement}")
else:
    st.info("Big or Small , every achievement counts! Share now ✨")

# footer
st.write("- - -")
st.write("🚀Keep believing in yourself for 🌟Bright Future🌟 Growth is a journey, not a destination!")
st.write("**💖 Created by REHMAT KHALID 💖**")
