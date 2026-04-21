from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    groq_api_key=st.secrets["GROQ_API_KEY"],
    model_name="llama-3.3-70b-versatile"
)

if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are")
    print(response.content)
