from openpyxl import Workbook


# 1- Criando o arquivo excel

wb = Workbook()

# 2- Nome do local do arquivo
name = 'files/test.xlsx'



# 4- Ativando o WorkSheet (documento)
ws1 = wb.active

# 5 - Alterando o titulo da planilha
ws1.title = 'Planilha1'

# 6 - Adicionando Dados
data = [
        ['Ano', 'Lucro', 'Custos'],
        [2021, '25%', '40%'],
        [2022, '45%', '50%'],
        [2023, '15%', '10%']
]

# Lendo os items da lista

for line in data:
    ws1.append(line)

# Adicionando uma outra planilha

ws2 = wb.create_sheet(title='Pi')
ws2['d2'] = 3.14




# Nome do arquivo
wb.save(filename=name)