import PyPDF2 as pdf
from PyPDF2 import PdfReader

def get_pdf_metadata(pdf_path):
     with open('pdf_path', 'rb') as f:
         reader = PdfReader(f)
         info = reader.metadata
     return info
 
 
 