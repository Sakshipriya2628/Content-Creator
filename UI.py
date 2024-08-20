from openai import OpenAI
from dotenv import load_dotenv
import os
from docx import Document
import fitz  # PyMuPDF
import streamlit as st

load_dotenv()

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(pdf_file) as pdf_document:
        num_pages = pdf_document.page_count
        for page_number in range(num_pages):
            page = pdf_document[page_number]
            text += page.get_text()
    return text

def extract_text_from_file(file_path):
    if file_path.name.lower().endswith('.docx'):
        print("Docx file detected.")
        return extract_text_from_docx(file_path)
    
    elif file_path.name.lower().endswith('.pdf'):
        print("Pdf file detected.")
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format. Supported formats: DOCX, PDF")
    
def gpt_call(content):
    prompt = f'''You are a professional content creator , who creates LinkedIn content . I am giving you the file {content} , you have to frame the 
         LinkedIn content which resembles to the {content} which I have passed. Also strictly remember that I'm a business which has created copilots
         using AI as technology. My motive is to promote my business to education providers and organisations by teaching them about the benefits of 
         AI in education field. 
         Strictly remember to make the first 2 lines of the content very pleasing to be read by anyone . The content length of LinkedIn post must not 
         exceed 4-5 lines and if increasing make sure to format it in proper paragraphs.
         Do not forget to give exciting hashtags and emoticons.'''
    client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
    conversation1 = [{"role": "system", "content": "You are an assistant, just answer and provide the required information to the user"},
                    {"role": "user", "content": prompt}]
    response1 = client.chat.completions.create(
            messages=conversation1,
            model="gpt-4",
            temperature=0
        )
    Output=response1.choices[0].message.content
    return Output

st.header("LinkedIn Content Creator") 
uploaded_file = st.file_uploader("Upload a file to create a LinkedIn post")
if uploaded_file is not None:
    file_text = extract_text_from_file(uploaded_file)
    button = st.button("Generate LinkedIn post")
    if button:
        with st.spinner("Generating LinkedIn post..."):
            st.write(gpt_call(file_text))