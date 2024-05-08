from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference, Series

wb = Workbook()

#  Ativação da planilha Sheet
ws = wb.active

data = [
    ['Ano', 'Lucro', 'Custos'],
    [2017, 40, 30],
    [2018, 35, 25],
    [2019, 30, 20],
    [2020, 10, 10],
    [2021, 15, 10],
    [2022, 25, 15]
    
]




