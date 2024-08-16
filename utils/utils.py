import os
import csv
import pandas as pd
from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_pdf(file_path):
    text = ""
    try:
        pdf_reader = PdfReader(file_path)
        for page in pdf_reader.pages:
            text += page.extract_text()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return text

def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return text

def check_keywords_in_text(text, keywords):
    for keyword in keywords:
        if keyword.lower() in text.lower():
            return True
    return False

def find_keywords_in_documents(keywords_file, folder_path, output_csv):
    # Load keywords from the text file
    with open(keywords_file, 'r') as f:
        keywords = [line.strip() for line in f.readlines()]
    
    matching_files = []

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if file_name.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file_name.endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:
            continue
        
        if check_keywords_in_text(text, keywords):
            print(f"Keyword found in: {file_name}")
            matching_files.append(file_name)
    
    # Save results to CSV
    if matching_files:
        df = pd.DataFrame(matching_files, columns=["File Name"])
        df.to_csv(output_csv, index=False)
        print(f"Results saved to {output_csv}")
    else:
        print("No matching files found.")