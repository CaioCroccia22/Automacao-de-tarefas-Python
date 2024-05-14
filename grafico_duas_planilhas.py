from openpyxl import Workbook, load_workbook
from openpyxl.chart import BarChart, Reference, Series


dict_ano = {}

# Importando despesas
arquivo1 = load_workbook(filename='files/despesas.xlsx')
ws1 = arquivo1['Planilha1']
max_linhas = ws1.max_row

for i in range(2, max_linhas+1):
    # print(ws1['A%s' %i].value)
    # print(ws1['B%s' %i].value)
    dict_ano[ws1['A%s' %i].value] = {'despesa':ws1['B%s' %i].value, 'receita':0}
    
# print(dict_ano)

# 2 - Importando Receita
arquivo2 = load_workbook(filename='files/Receitas.xlsx')
ws2 = arquivo2['Planilha1']
max_linhas = ws1.max_row
for i in range(2, max_linhas+1):
    # print(ws1['A%s' %i].value)
    # print(ws1['B%s' %i].value)
    dict_ano[ws2['A%s' %i].value]['receita'] = ws2['B%s'%i].value
    
print(dict_ano)