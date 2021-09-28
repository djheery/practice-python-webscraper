from pprint import pp, pprint
from openpyxl import Workbook
from openpyxl.worksheet.page import PrintOptions

# Setup
wb = Workbook()
ws = wb.active
ws.title = 'Actors'

def insert_name(c, data):
  c.value = data
  return

def insert_email(row, data):
  print(row)
  return


def insert_website(row, data):
  return

def insert_location(row, data):
  return

def insert_about(row, data):
  return

def create_titles(): 
  ws['A1'] = 'Name'
  ws['B1'] = 'Email'
  ws['C1'] = 'Website'
  ws['D1'] = 'Location'
  ws['E1'] = 'About'


def populate_sheet(data):
  rows = ws.iter_rows(min_row=1, max_row=len(data), max_col=len(data[0]))
  i = 0
  for  row in rows:
    for cell in row:
      pprint(cell.row)
      pprint(i)
      if cell.row == 1: insert_name(cell, data[i]['name'])
      if cell.row == 2: insert_name(cell, data[i]['name'])
      if cell.row == 3: insert_name(cell, data[i]['name'])
      if cell.row == 4: insert_name(cell, data[i]['name'])
      if cell.row == 5: insert_name(cell, data[i]['name'])
      i = i + 1
      pprint(cell.value)
  return
