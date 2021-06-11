import pandas as pd
from scipy.stats import skew


class Information:
    
    def __init__(self, df) -> None:
        self.df = df
        
    def information(self):
        x = list(zip(self.df.count(), self.df.dtypes, (self.df.isnull().sum() / self.df.shape[0])))
        y = dict(zip(self.df.columns, x))
        return pd.DataFrame(y, index=['Number of Values', 'Data Type', 'Perc Null']).transpose()
    
    def skew(self):
        cols = self.df.select_dtypes('number').columns
        skews = skew(self.df[cols], nan_policy='omit').data
        
        return pd.DataFrame(dict(zip(cols, skews)), index=['skew'])

    
    def corr(self):
        return self.df.corr()
    
    
    def describe(self):
        return self.df.describe().transpose()