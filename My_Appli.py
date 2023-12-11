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
    Tell me the story.
    The lenght of the story must be less than 100 words.
    And then make 5 question in a JSON array from the story you wrote, one question per line.
    Each question should have 2 fields:
    - "Question" -the question you make from the story
    - "Answer" -the answer for the question
    """
    
st.title('Write a story and Make questions')
st.markdown('Input your words.\n\
        The AI will write a story from the words you gave \n\
        and then you wil get 5 questions from the story, along with their answer.')

user_input = st.text_area("Enter 2-5 words. Use the colon to separate each words. For the example: bee, flower, eat")

# submit button after text input
if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    # Show the response from the AI in a box
    st.markdown('**AI response:**')
    suggestion_dictionary = response.choices[0].message.content


    sd = json.loads(suggestion_dictionary)

    print (sd)
    suggestion_df = pd.DataFrame.from_dict(sd)
    print(suggestion_df)
    st.table(suggestion_df)
    






