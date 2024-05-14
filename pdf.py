import PyPDF2 as pdf
from PyPDF2 import PdfReader


# 1 - Versão e Métodos dessa biblioteca
# print(pdf.__version__)


# 2 - Obter metodos disponiveis
# print(dir(pdf))

# 3 - Importando o arquivo PDF
file = open('files/Diploma.pdf', 'rb')
reader = PdfReader(file)
print(reader)
print(reader.metadata)

info = reader.metadata

# 4 - Extraindo algumas informações
print(info.title)
print(info.author)
print(info.creator)
print(info.subject)
print(len(reader.pages))
print(reader.pages[0].extract_text())
print(reader.pages[1].extract_text())
