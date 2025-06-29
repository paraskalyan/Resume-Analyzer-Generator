import os
import streamlit as st
from dotenv import load_dotenv

from openai import OpenAI
client = OpenAI()

load_dotenv()  # loads .env file

client.api_key = os.getenv("OPENAI_API_KEY")


def generate_custom_resume(resume_text, job_description):
    prompt = f"""
You are a professional resume editor. Customize the resume below to better fit the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return a new version of the resume tailored to the job.
"""
    response = client.responses.create(
         model="gpt-4.1",
        input=[{"role": "user", "content": prompt}]
    )
    print(response)


resume_text = open("resume.txt", "r").read()
job_description=open("job-desc.txt", "r").read()
generate_custom_resume(resume_text, job_description)

# Streamlit UI
# st.title("AI Resume Customizer")

# resume_text = open("resume.txt", "r").read()

# job_description = st.text_area("Paste Job Description")

# if st.button("Generate Tailored Resume"):
#     with st.spinner("Generating..."):
#         new_resume = generate_custom_resume(resume_text, job_description)
#         st.text_area("Tailored Resume", new_resume, height=400)
