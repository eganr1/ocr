# Source: https://medium.com/social-impact-analytics/extract-text-from-unsearchable-pdfs-for-data-analysis-using-python-a6a2ca0866dd

# import libraries
import ocrmypdf
import os
import pandas as pd
import fitz #!pip install PyMuPDF

# get pdf files
PATH = os.getcwd()
file_list = [f for f in os.listdir(path=PATH) if f.endswith('.pdf') or f.endswith('.PDF')]
#file_list = [f for f in os.listdir(path="ocr_success/") if f.endswith('.pdf') or f.endswith('.PDF')]
file = "A_Social_Problem_In_Jungle_Ter.pdf"
'''
main ocr code, which create new pdf file with OCR_ ahead its origin filename, 
and error messege can be find in error_log
'''

# %%time
error_log = {}
for file in file_list:
    try:
        result = ocrmypdf.ocr(file, 'OCR_'+file,output_type='pdf',skip_text=True,deskew=True)
    except Exception as e:
        if hasattr(e,'message'):
            error_log[file] = e.message
        else:
            error_log[file] = e
        continue
        
'''
extract OCRed PDF using PyMuPDF and save into a pandas dataframe
'''
ocr_file_list = [f for f in os.listdir(path=PATH) if f.startswith('OCR_') ]

# PDF extraction
# informations we want to extract
extraction_pdfs = {}

for file in ocr_file_list:
    #save the results
    pages_df = pages_df = pd.DataFrame(columns=['text'])
    # file reader
    doc = fitz.open(file)
    for page_num in range(doc.pageCount):
        page = doc.loadPage(page_num)
        pages_df = pages_df.append({'text': page.getText('text')}, ignore_index=True)
        
        extraction_pdfs[file] = pages_df