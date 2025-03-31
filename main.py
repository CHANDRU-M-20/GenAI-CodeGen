from model import LLM
import streamlit as st


st.header("Google Gemini LLM")
st.write("This is a simple Streamlit app to interact with Google Gemini LLM.")

genai_model = LLM("gemini-1.5-pro")
print("LLM initialized successfully.")
llm = genai_model.get_llm()

input = st.text_input("Enter your query:", key="query_input") 

if st.button("Submit"):
    response = llm.invoke(input)

    st.write("Response from LLM:")
    st.write(response.content)
    print(response.content)

