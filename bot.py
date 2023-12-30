import streamlit as st
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain.chat_models import ChatOpenAI
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = 
logo_path = "your_logo.png"  # Replace with the path to your logo image
st.sidebar.image(logo_path, width=200)

# Chatbot title
st.title('Text To SQL ChatBOT')

# Sidebar with services and solutions
st.sidebar.title("Services & Solutions")
st.sidebar.header("AI Consulting & Full Stack Development")
st.sidebar.markdown("- Natural Language Processing (NLP)")
st.sidebar.markdown("- Computer Vision")
st.sidebar.markdown("- Forecasting")
st.sidebar.markdown("- Speech to Text & Text to Speech")
st.sidebar.markdown("- ChatGPT Integration")
st.sidebar.markdown("- Robotic Process Automation")
st.sidebar.markdown("- Web and Mobile App Development")

# Link to BotKernel
st.sidebar.header("About US")
st.sidebar.markdown("[BotKernel](https://www.botkernel.com/)")

# Load the database
db = SQLDatabase.from_uri("sqlite:///northwind.db")

# Create the language model and SQL query chain
llm = OpenAI(temperature=0, verbose=True)
chain = create_sql_query_chain(ChatOpenAI(temperature=0), db)

user_question = st.text_area('You:', height=100)

if st.button('Send'):
    if user_question:
        # Get the response from the chain based on user input
        response = chain.invoke({"question": user_question})

        # Display user query with user icon and color
        st.markdown(
            f'<div style="background-color: #d8eafd; padding: 10px; border-radius: 5px;">👤 You: {user_question}</div>',
            unsafe_allow_html=True
        )

        # Execute db.run(response)
        db_response = db.run(response)

        # Display the bot's response with bot icon and color including db_response
        st.markdown(
            f'<div style="background-color: #e6ffe6; padding: 10px; border-radius: 5px;">🤖 SQL Query: {response}<br><br>Anwser From DB:<br>{db_response}</div>',
            unsafe_allow_html=True
        )
    else:
        st.write("Please enter a question.")

