import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter
import os

def get_pdf_metadata(pdf_path):
     with open(pdf_path, 'rb') as f:
         reader = PdfReader(f)
         info = reader.metadata
     return info
 
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        results = []
        for i in range(0, len(reader.pages)):
            selected_pages = reader.pages[i]
            text = selected_pages.extract_text()
            results.append(text)
        return ' '.join(results)


def split_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            selected_pages = reader.pages[page_num]
            writer = PdfWriter()
            writer.add_page(selected_pages)
            output_filename = os.path.join(
                os.path.dirname(pdf_path), 
                f'page_{page_num + 1}.pdf'
            )
            with open(output_filename, 'wb') as output_pdf:
                writer.write(output_pdf)
            print(f'Page {page_num + 1} saved as {output_filename}')

# 1 - Buscando Dados e Metadados de um arquivo PDF
# print(get_pdf_metadata('files/Diploma.pdf'))
# print(get_pdf_metadata('files/Diploma.pdf'))
# print(extract_text_from_pdf('files/Diploma.pdf'))

# 2 - Dividindo pdf por página
split_pdf('files/Diploma.pdf')
