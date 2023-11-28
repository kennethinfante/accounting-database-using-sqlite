from xlrd import open_workbook
import csv

wb = open_workbook('service_type_business.xlsx')

for i in range(0, wb.nsheets):
    sheet = wb.sheet_by_index(i)
    print(sheet.name)
    # newline="" to remove blank lines
    with open("db_data/%s.csv" %(sheet.name.replace(" ","")), "w", newline="") as file:
        writer = csv.writer(file, delimiter = ",")
        print(sheet, sheet.name, sheet.ncols, sheet.nrows)

        # do not include rows for command line import
        # header = [cell.value for cell in sheet.row(0)]
        # writer.writerow(header)

        for row_idx in range(0, sheet.nrows):
            row = [int(cell.value) if isinstance(cell.value, float) else cell.value
                   for cell in sheet.row(row_idx)]

            writer.writerow(row)