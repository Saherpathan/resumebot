import os
from dotenv import load_dotenv
import streamlit as st
import PyPDF2
import cohere
from dotenv import load_dotenv

#Load env variables from .env file
load_dotenv()

# Initialize Cohere API (make sure to use your actual API key)
cohere_client = cohere.Client(os.getenv('cohere-api-key'))

# Define the function to extract text from Resume PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""  
    return text

# Function to generate response from Cohere
def generate_response(prompt):
    response = cohere_client.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=1500,  
    )
    return response.generations[0].text.strip()

# Chatbot interface using Streamlit
st.title("RESUME CHATBOT")
st.write("Upload your resume to start a conversation")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.write("Resume Uploaded. Here's a preview:")
    st.text_area("Resume Text", resume_text, height=200)

    # Initialize chat context
    if "context" not in st.session_state:
        st.session_state["context"] = []

    # Chat input
    user_input = st.text_input("Ask about the candidate:")

    if user_input:
        # Append the user input to the context
        st.session_state["context"].append({"user": user_input})

        # Construct the prompt using the resume text and the context
        # Here the context prompt section will account for incorporating the chat history context to further responses
        context_prompt = "\n".join([f":User  {entry['user']}\nBot: {entry.get('bot', '')}" for entry in st.session_state["context"]])
        prompt = f"Here is the resume:\n\n{resume_text}\n\n{context_prompt}\nUser  question: {user_input}\n\nBot reply:"

        # Generate the bot's reply
        bot_reply = generate_response(prompt)

        # Append the bot's reply to the context
        st.session_state["context"][-1]["bot"] = bot_reply

        # Display the bot's reply
        st.write(f"Bot: {bot_reply}")


    # st.write("Context:", st.session_state["context"])
