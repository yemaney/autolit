import pandas as pd

class Type_Check:
    
    def __init__(self, df) -> None:
        self.df = df
    
    def numeric(self):
        return self.df.select_dtypes('number')
    
    def categorical(self):
        return self.df.select_dtypes('object')
    
    def datetime(self):
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                try:
                    self.df[col] = pd.to_datetime(self.df[col], infer_datetime_format=True)
                except:
                    pass
        return self.df.select_dtypes('datetime')