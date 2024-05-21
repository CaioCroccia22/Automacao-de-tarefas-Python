import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
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


def split_pdf_page(pdf_path,start_page:int=0, stop_page:int=0):
    with(open(pdf_path, 'rb')) as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        for page_num in range(start_page, stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            # print(start_page)
            # print(stop_page)
            new_filename = f'files/{filename}_from_{start_page}_to_{stop_page}.pdf'
            with open(new_filename, 'wb') as out:
                writer.write(out)



def merge_pdf(list_pdfs, output_filename='files/final_pdf.pdf'):
    merger = PdfMerger()
    with open(output_filename, 'wb') as f:
        for file in list_pdfs:
            merger.append(file)
        merger.write(f)
        
        

def rotate_pdf(pdf_path, page_num: int, rotation: int=90):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        writer.pages[page_num].rotate(rotation)
        filename = os.path.split(pdf_path)[1]
        new_filename = f'files/{filename}_{rotation}_page_rotated.pdf'
        with open(new_filename, 'wb') as out:
            writer.write(out)
            
            
            
# Função para extrair imagens do PDF
def extract_images_from_pdf(pdf_path):
    with open(pdf_path,'rb') as f:
        reader = PdfReader(f)
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            # print(selected_page.images)
            for img_file_obj in selected_page.images:
                with open(f'files/{img_file_obj.name}', 'wb') as out:
                    out.write(img_file_obj.data)
                    
                          



# 1 - Buscando Dados e Metadados de um arquivo PDF
# print(get_pdf_metadata('files/Diploma.pdf'))
# print(get_pdf_metadata('files/Diploma.pdf'))
# print(extract_text_from_pdf('files/Diploma.pdf'))

# 2 - Dividindo pdf por página
# split_pdf('files/Diploma.pdf')


# 3 - Dividindo o PDF por página selecionada
# split_pdf_page('files/Diploma.pdf',1,2)


# Unido os PDFS
# merge_pdf(['files/page_1.pdf','files/page_1.pdf'])

# 5 - Rotacionando PDF
# rotate_pdf('files/page_1.pdf', 0, 180)

# 6 - Extraindo Imagem em PDF
extract_images_from_pdf('files/chart.pdf')