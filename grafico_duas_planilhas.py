from openpyxl import Workbook, load_workbook
from openpyxl.chart import BarChart, Reference,series


dict_ano = {}

# Importando despesas
arquivo1 = load_workbook(filename='files/despesas.xlsx')
ws1 = arquivo1['despesas']
max_linhas = ws1.max_row

for i in range(2, max_linhas+1):
    print(ws1['A%s' %i].value)