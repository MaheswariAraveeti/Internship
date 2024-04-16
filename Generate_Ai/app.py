import streamlit as st
from openai import OpenAI

f = open(r"C:\Users\Welcome\internship_assainments\Gen_Ai_Task\gen_ai_key.txt")
OPENAI_API_KEY = f.read()

st.title("Genarative Ai For Code Review")
st.subheader("Correcting the Bugs and Errors In the Given Code")

client = OpenAI(api_key = OPENAI_API_KEY)

prompt = st.text_area("Enter a Code")

if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "As a code review expert, your task is to identify bugs and errors in code and provide corrected versions. Your expertise ensures code quality and helps developers improve their skills."},
        {"role": "user", "content": prompt}
      ]
    )
    st.write(response.choices[0].message.content)