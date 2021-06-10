import pandas as pd
from scipy.stats import skew


class Stat_Check:
    
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        
    def skew(self):
        cols = self.df.select_dtypes('number').columns
        skews = skew(self.df[cols], nan_policy='omit').data
        
        return pd.DataFrame(dict(zip(cols, skews)), index=['skew'])

    
    def corr(self):
        return self.df.corr()