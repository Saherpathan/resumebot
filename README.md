# Resume Chatbot 🤖✨

A Streamlit-based chatbot that interacts with users about candidate's resumes by extracting information from uploaded PDF files and generating responses using the Cohere API.

## Features 🌟

- Upload and parse PDF resumes
- Interactive chat interface
- Context-aware responses based on chat history and resume content
- Utilizes the Cohere API for generating intelligent replies

## Prerequisites ⚙️
**Before you begin, ensure you have the following installed:**

- Python 3.x
- pip (Python package manager) 📦

## Installation 🛠️

Follow these steps to set up the project locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/Saherpathan/resumebot.git
   cd resumebot
   
2. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   
3. **Set up environment variables**
   ```bash
   cohere-api-key=your_cohere_api_key

Make sure to replace your_cohere_api_key with your actual API key from the Cohere dashboard.

## Usage 🚀

To run the chatbot locally, execute the following command:

```bash
streamlit run pdfparser.py
```

## Demo 🎥

Here's a quick demonstration of how the Resume Chatbot works:

1. **Upload your Resume**: The chatbot allows candidate to upload resume in PDF format.
   
   ![image](https://github.com/user-attachments/assets/d74bf162-8403-4b42-8081-94f20af07479)


2. **Interactive Chat**: After uploading, one can ask questions about the candidate, and the chatbot will respond based on the resume content as well as contextual chat history.

   ![image](https://github.com/user-attachments/assets/aae46092-8e52-444b-98a4-cbe439154fb6)
   ![image](https://github.com/user-attachments/assets/c2adaaf3-885a-432c-be86-168f947e9037)


The screenshots above illustrate the main functionalities of the Resume Chatbot, showcasing the user-friendly interface and the interaction flow.
