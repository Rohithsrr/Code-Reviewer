import streamlit as st
import google.generativeai as genai

# Set API keys (Replace with your actual API keys)
GOOGLE_API_KEY = "<YOUR GOOGLE API KEY HERE>"
genai.configure(api_key=GOOGLE_API_KEY)

def review_code_gemini(code):
    """Analyze code using Gemini AI API."""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Review and fix the following Python code:\n\n{code}")
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("AI Code Reviewer")

st.write("Paste your Python code below and select an AI model for review.")
code_input = st.text_area("Enter your Python code here:", height=250)
model_choice = st.selectbox("Choose AI Model", ["Google Gemini-Pro"])

if st.button("Review Code"):
    if code_input.strip():
        st.write("### Review Results")
        with st.spinner("Analyzing your code..."):
            if model_choice == "OpenAI GPT-4":
                review_result = review_code_openai(code_input)
            else:
                review_result = review_code_gemini(code_input)
        st.markdown(f"```markdown\n{review_result}\n```")
    else:
        st.warning("Please enter some Python code for review.")

st.write("---")
st.write("Developed by Putha Sai Rohith Reddy - AI Code Reviewer using Gemini APIs")
