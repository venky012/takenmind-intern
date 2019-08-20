import pandas as pd

#xlrd
#openpyxl

excelfile = pd.ExcelFile('demo2.xlsx')
dframe = excelfile.parse('demo2')
print dframe