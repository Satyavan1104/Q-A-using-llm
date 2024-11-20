import cohere
import streamlit as st
import os

# Initialize the Cohere client
cohere_api_key = os.getenv("Mrh9BFF0YcKhl4jp5JC7ijKj0JwpQXdKFiz2aWm4")  # Make sure to set your API key in .env or elsewhere
co = cohere.Client(cohere_api_key)

## Function to load Cohere model and get response
def get_cohere_response(question):
    response = co.generate(
        model="xlarge",  # You can specify other models based on your use case
        prompt=question,
        max_tokens=100,  # Adjust the max tokens as needed
        temperature=0.5  # Adjust temperature to control randomness
    )
    return response.generations[0].text.strip()  # Return the first generation

## Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Cohere Q&A Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## If the button is clicked
if submit:
    if input:
        response = get_cohere_response(input)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.warning("Please enter a question.")
