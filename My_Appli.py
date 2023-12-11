#Write a story from user's words and make questions

import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """
        Act as a writer. 
        You will recieve words and you should write a story from these words.
        And then make 7 question from the story you wrote in a JSON array, one question per line.
        Each question should have 3 fields:
        - "Question" -the question you make from the story
        - "Answer" -the answer for the question
        """
        
st.title('Write a story and Make questions')
st.markdown('Input your words.\n\
            The AI will write a story from the words you gave \n\
            and then you wil get 10 questions from the story, along with their answer.')

user_input = st.text_area("Enter 2-10 words. Use the colon to separate each words. For the example: bee, flower, eat")



if st.button("Submit"):
    if user_input:
        response = client.complete(
            engine="text-davinci-003",
            prompt=prompt + "\n\n" + user_input,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            log_level="info",
        )
        output = response.choices[0].text.strip()
        st.text_area("Output", value=output, height=200)
    else:
        st.warning("Please enter some words before submitting.")

