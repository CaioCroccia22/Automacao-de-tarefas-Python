from openpyxl import Workbook

print('Lendo dados do arquivo de texto')

file_txt = open('files/gastos.txt', 'r', encoding='utf-8')
file = file_txt.read()
# print(file)
# Coloca os valores dentro de uma lista
list_data = file.splitlines()
print(list_data)

# Iterando os valores da lista
for i in range(0, len(list_data)):
    list_data[i] = list_data[i].split(',')
    
# Criando planilha
wb = Workbook()
ws = wb.active

for row in list_data:
    ws.append(row)
    
wb.save('files/gastos.xlsx')