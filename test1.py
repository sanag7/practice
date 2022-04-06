import csv
import pandas as pd
from Convertor import XlsxToCsv

xlsx_path = "/Users/hwanju/Documents/성당/성소후원회 명단.xlsx"
# dir, file_name = os.path.split(xlsx_file_path)

# print(dir)

# xlsx = pd.read_excel(xlsx_file_path)
# csv_file_path = os.path.join(dir,"성소후원회명단.csv")
# print(csv_file_path)
# # xlsx.to_csv(csv_file_path)

# csv_from_xlsx = pd.read_csv(csv_file_path)
# print (csv_from_xlsx)



# def XlsxToCsv(xlsx_path) :
#     dir, file_name = os.path.splitext(xlsx_path)
#     xlsx = pd.read_excel(xlsx_path)
#     csv_path = os.path.join(dir, ".csv")
#     xlsx.to_csv(csv_path)
#     print(f'csv 파일경로 : {csv_path}')


XlsxToCsv(xlsx_path)
