from openpyxl import Workbook
from pprint import pp, pprint

filename = "practice_sheet.xlsx"
wb = Workbook()
ws = wb.active

def print_rows():
  for row in ws.iter_rows(values_only=True):
    pprint(row)

ws['A1'] = 'Hello'
ws['B1'] = 'World'

wb.save(filename=filename)

cell = ws['A1']
# cell.value = 'Bitch'

print_rows()

ws.insert_cols(idx=1)
print_rows()

ws.insert_cols(idx=3, amount=5)
print_rows()

ws.delete_cols(idx=3, amount=5)
ws.delete_cols(idx=1)
print_rows()

ws.insert_rows(idx=1)
print_rows()
ws.insert_rows(idx=1, amount=3)
print_rows()