#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import re
import pandas as pd

def extract_emails(text):
    return re.findall(r'[^@\s]+@[^@\s]+\.[^@\s]+', text)

def extract_phone_numbers(text):
    return re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)

#----------------------------------------------------------------

import PyPDF2

def pdf_to_txt(pdf_path, txt_path):
    """
    Converts a PDF file to a plain text (.txt) file.
    :param pdf_path: Path to the input PDF file
    :param txt_path: Path to save the output text file
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_text = ''
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(pdf_text)

    print(f"Converted {pdf_path} to {txt_path}")

# Example usage
#pdf_file_path = r"C:\Users\hp\Downloads\Sample2-20240406T093029Z-001\pdf_files\AarushiRohatgi.pdf"  # Replace with your PDF file path
pdf_file_path = input("enter the file path")

txt_file_path = 'cv1.txt'  # Replace with the desired output text file path
pdf_to_txt(pdf_file_path, txt_file_path)

#------------------------------------------------------------------------------------


# Read CV files (assuming they are in the same directory)
cv_files = ['cv1.txt']  # Replace with actual filenames
cv_data = []

for filename in cv_files:
    with open(filename, 'r',encoding='utf-8') as cv_file:
        cv_text = cv_file.read()
        emails = extract_emails(cv_text)
        phone_numbers = extract_phone_numbers(cv_text)
        cv_data.append({
            'Email': ', '.join(emails),
            'Phone': ', '.join(phone_numbers),
            'Overall Text': cv_text
        })

# Create a DataFrame
new_data = pd.DataFrame(cv_data)

# Save to .xls format
output_file = 'cv_data1.xls'

if os.path.exists(output_file):
    # If it exists, read the existing data
    existing_data = pd.read_excel(output_file)
    # Append the new data
    df = pd.concat([existing_data, new_data], ignore_index=True)
else:
    # If it doesn't exist, use the new data
    df = new_data


df.to_excel(output_file, index=False)
print(f"Data saved to {output_file}")


# In[ ]:




