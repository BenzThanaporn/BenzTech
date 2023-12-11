#Child Naming Application

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
st.markdown('Input 2-10 words.\n\
            The AI will write a story from the words you gave \n\
            and then you wil get 10 questions from the story, along with their answer.')

user_input = st.text_area("Enter 2-10 words.Use colon to separate each words.\n\
    For the example: bee, flower, eat")
