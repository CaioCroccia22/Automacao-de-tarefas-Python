from openpyxl import Workbook


# 1- Criando o arquivo excel

wb = Workbook()

# 2- Nome do local do arquivo
name = 'files/test.xlsx'

# 3- Nome do arquivo
wb.save(filename=name)

