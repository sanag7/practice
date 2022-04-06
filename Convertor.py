import pandas as pd
import os



def __init__(self) -> None:
        pass


def XlsxToCsv(xlsx_path) :
        dir, file_name = os.path.splitext(xlsx_path)
        xlsx = pd.read_excel(xlsx_path)
        csv_path = os.path.join(dir + ".csv")
        xlsx.to_csv(csv_path)
        print(f'csv 파일경로 : {csv_path}')

