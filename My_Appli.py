import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")
#user_api_key = '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'
#user_api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
#client = openai.ChatCompletion.create(api_key=user_api_key)

#user_api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
#client = openai.api_key = user_api_key

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as a Korean-English-Thai translator. You will receive a 
            Korean text and you should give the translation in English and Thai.
            You will translate the text into English first and then translate the English text into Thai.
            If the given text is already in English, you should translate it into Thai directly.
            List the translation in a JSON array, one translation per line.
            Each translation should have 3 fields:
            - "Korean Original Text" - the Korean original text before the translation
            - "English Translation" - the text translated into English
            - "Thai Translation" - the text translated into Thai
            For example:
            [
                {
                    "Korean Original Text": "안녕하세요. 저는 한국어를 배우고 있습니다.",
                    "English Translation": "Hello. I am learning Korean.",
                    "Thai Translation": "สวัสดีค่ะ ฉันกำลังเรียนภาษาเกาหลี"
                },
                {
                    "Korean Original Text": "안녕하세요. 저는 한국어를 배우고 있습니다.",
                    "English Translation": "Hello. I am learning Korean.",
                    "Thai Translation": "สวัสดีค่ะ ฉันกำลังเรียนภาษาเกาหลี"
                }
            ]
        """    


st.title('We go Korean')
st.subheader('Korean-English-Thai translator')
st.markdown('Input the text that you want to translate. \n\
            The AI will translate it for you.')

user_input = st.text_area("Enter some text to correct:", "Your text here")


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
    






