# LinkedIn Content Creator

This project is a Streamlit-based web application that generates LinkedIn posts from the content of uploaded DOCX or PDF files. It leverages the OpenAI GPT model to create professional, engaging LinkedIn content tailored for businesses in the AI education sector.

## Features

- **File Upload**: Upload DOCX or PDF files to extract their content.
- **Text Extraction**: Automatically extracts text from DOCX and PDF files using Python libraries.
- **Content Generation**: Generates concise and engaging LinkedIn posts based on the extracted content using OpenAI's GPT-4 model.
- **User-Friendly Interface**: Simple and intuitive interface provided by Streamlit.

## Requirements

- Python 3.7+
- Required Python packages: Install via `pip install -r requirements.txt`
  - `openai`
  - `python-dotenv`
  - `python-docx`
  - `pymupdf` (PyMuPDF)
  - `streamlit`

## Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Code Overview

### File Structure

- **`app.py`**: Main application file that contains all the logic for the Streamlit app.
- **`.env`**: Environment file to store sensitive information like API keys.

### Key Functions

- `extract_text_from_docx(docx_file)`: Extracts text from DOCX files.
- `extract_text_from_pdf(pdf_file)`: Extracts text from PDF files.
- `extract_text_from_file(file_path)`: Determines the file type and extracts text accordingly.
- `gpt_call(content)`: Makes a call to the OpenAI API to generate a LinkedIn post from the extracted content.

### Streamlit Interface

- **Header**: Displays the title of the application.
- **File Uploader**: Allows users to upload DOCX or PDF files.
- **Generate Button**: Once the file is uploaded, clicking this button will generate the LinkedIn post using GPT-4.

## Usage

1. Upload a DOCX or PDF file using the file uploader in the Streamlit app.
2. Click the "Generate LinkedIn post" button.
3. Wait for the LinkedIn post to be generated and displayed on the screen.
