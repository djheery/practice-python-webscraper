from pprint import pprint
from openpyxl import Workbook
from openpyxl import worksheet
import datetime

wb = Workbook()
ws = wb.active
ws.title = 'Hello World'

print(ws.title)