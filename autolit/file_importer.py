import pandas as pd


class File:
    """Class used to handle the importing of tabular data in the streamit app
    
    Args:
        file (str): filpath, or url to tabular information
    """ 
    
    def __init__(self, file) -> None:
        self.file = file
    
    def import_csv(self, sep: str):
        """Used to read and import csv files into the app

        Args:
            sep (str): delimiter that seperates values in the csv

        Returns:
            pandas dataframe: Dataframe of the csv
        """
        return pd.read_csv(self.file, sep)
    
    def xls_sheets(self):
        """Method to get xls sheetnames

        Returns:
            list: list of sheetnames in the xls file
        """
        return pd.ExcelFile(self.file).sheet_names
    
    def import_xls(self, sheet_name):
        """Used to read and import xls files

        Args:
            sheet_name (str): name of the sheet to read and import

        Returns:
            pandas dataframe: Dataframe of the xls sheet 
        """
        return pd.ExcelFile(self.file).parse(sheet_name=sheet_name)