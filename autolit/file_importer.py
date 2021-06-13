import pandas as pd


class File:
    
    def __init__(self, file) -> None:
        self.file = file
    
    def import_csv(self, sep: str):
        return pd.read_csv(self.file, sep)
    
    def xls_sheets(self):
        return pd.ExcelFile(self.file).sheet_names
    
    def import_xls(self, sheet_name):
        return pd.ExcelFile(self.file).parse(sheet_name=sheet_name)