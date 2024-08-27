import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai_api_key = st.secrets["openai"]["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_api_key)

def ask_gpt4o_mini(question):
    responses = []
    for _ in range(3):
        response = client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:raptive-nonprod:tess-test:9qmuyReT",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for Handle the Heat. Your goal is to respond to comments from our users. Do not under any circumstances use proper names in your responses."},
                {"role": "user", "content": question}
            ]
        )
        responses.append(response.choices[0].message.content)
    return responses

def main():
    st.markdown("<h1 style='text-align: right; color: red;'>PRIVATE AND CONFIDENTIAL</h1>", unsafe_allow_html=True)
    st.title("Handle the Heat Comment Bot")
    st.write("This is an AI-powered comment bot for Handle the Heat. Please note that AI models can sometimes be incorrect or provide unexpected responses.")
    st.warning("Do not share this site publicly. It is intended for internal use only.")

    # Post title input
    post_title = st.text_input("Enter the post title (optional):")

    # User input
    user_question = st.text_area("Enter the comment:")

    if st.button("Generate Responses"):
        if user_question:
            with st.spinner("Generating answers... This may take a while."):
                try:
                    # Append the title to the question if provided
                    full_question = f"Title: {post_title}\n{user_question}" if post_title else user_question
                    answers = ask_gpt4o_mini(full_question)
                    for i, answer in enumerate(answers, 1):
                        st.subheader(f"Response Option {i}:")
                        st.write(answer)
                except Exception as e:
                    st.error(f"Error generating answers: {str(e)}")
        else:
            st.write("Please enter a comment.")

if __name__ == "__main__":
    main()