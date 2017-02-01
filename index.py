import xlrd

workbook = xlrd.open_workbook('example.xlsx')
sheet_names = workbook.sheet_names()
sheet = workbook.sheet_by_name(sheet_names[0])

for row_idx in range(sheet.nrows):
	for col_idx in range(sheet.ncols):
		cell = sheet.cell(row_idx, col_idx)
		print(cell.value, end="\t")
print()