# Initialize OpenAI Embeddings
import streamlit as st
from langchain_openai import OpenAIEmbeddings

# Retrieve API key from Streamlit Secrets
openai_api_key = st.secrets["openai"]["api_key"]

# Initialize OpenAI Embeddings
embeddings_model = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Display confirmation message in Streamlit
st.write("OpenAI API Key successfully retrieved from Streamlit Secrets!")

# Define PHASES before calling main()
PHASES = {
    "phase1": {
        "name": "What is your name?",
        "fields": {
            "name": {
                "type": "text_input",
                "label": "What is your first name?",
            },
            "saint": {
                "type": "text_input",
                "label": "Who is your favorite saint?"
            }
        },
        "user_prompt": "My name is {name} and I love {saint}. Write a poem about my favorite saint.",
    },
}

#  Import core_logic AFTER setting up API key
from core_logic.main import main  

if __name__ == "__main__":
    # Pass OpenAI API Key in config
    main(config={"phases": PHASES, "openai_api_key": openai_api_key})

