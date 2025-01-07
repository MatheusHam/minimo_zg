import datetime

import streamlit as st
import pandas as pd

import transformers
import torch


st.set_page_config(
    page_title="Zeitgeist",
    page_icon="🔮", 
    layout="wide"
)

st.title("Zeitgeist")

end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=30)

st.sidebar.date_input(
    "Select Start Date",
    value=start_date, 
    min_value=None, max_value=None, key="start_date")

st.sidebar.date_input(
    "Select End Date",
    value=end_date, 
    min_value=None, max_value=None, key="end_date")


# @st.cache_data
# def load():
#     return pd.read_csv("data.csv")



def execute():
    model_id = "meta-llama/Llama-3.2-3B-Instruct"

    pipeline = transformers.pipeline(
        "text-generation",
        model=model_id,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto",
    )

    messages = [
        {
            "role": "system", 
            "content": system_prompt
        },
        {
            "role": "user", 
            "content": user_prompt
        },
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=256,
    )
    
    st.text_area("teste",outputs[0]["generated_text"][-1]['content'])
    
    
system_prompt = st.text_input("System Prompt", "Fala como se fosse um mano de osasco")
user_prompt = st.text_input("User Prompt", "cinco curiosidades sobre o osasco")

if st.button("Run"):
    execute()