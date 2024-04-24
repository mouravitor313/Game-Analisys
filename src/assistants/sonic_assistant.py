import openai
import pandas as pd
import os

API_KEY = os.getenv("API_KEY_OPENAI")
openai.api_key = API_KEY

def collect_information_and_analyze(prompt):

    data=pd.read_csv('data/games_data_output')
    completions = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "user", "content": prompt+"\n\n"+data}
        ],
        temperature=0.3,
    )
    message_received_from_model = completions.choices[0].message.content
    return message_received_from_model
