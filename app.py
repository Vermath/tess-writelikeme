import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai_api_key = st.secrets["openai"]["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_api_key)

# Define the models
models = {
    "Write Like Me v2": "ft:gpt-4o-mini-2024-07-18:raptive-nonprod:hth-writelikemev2:9rV5LOAo",
    "Write Like Me v1": "ft:gpt-4o-mini-2024-07-18:raptive-nonprod:hth-writelikeme:9rTBzO6k"
}

def ask_gpt4o_mini(question, model):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for Hand the Heat. You rewrite freelancer content to be in the Handle the Heat style. Be sure to format the content beautifully. Use markdown formatting throughout."},
            {"role": "user", "content": question}
        ],
        max_tokens=4000  # Set the maximum token output to 16k
    )
    return response.choices[0].message.content

def main():
    st.title("HTH Write Like Me")

    # Model selection
    selected_model = st.selectbox("Choose a model:", list(models.keys()))

    # User input
    user_question = st.text_input("Enter a comment to respond to:")

    if st.button("Generate Response"):
        if user_question:
            with st.spinner("Generating response... This may take a while."):
                try:
                    answer = ask_gpt4o_mini(user_question, models[selected_model])
                    st.subheader("Response:")
                    st.markdown(answer)  # Use st.markdown() to render the markdown
                except Exception as e:
                    st.error(f"Error generating response: {str(e)}")
        else:
            st.write("Please enter a comment.")

if __name__ == "__main__":
    main()