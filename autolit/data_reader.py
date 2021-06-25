import pandas as pd


class Information:
    
    def __init__(self, df) -> None:
        self.df = df
        
    def information(self):
        x = list(zip(self.df.count(), self.df.dtypes, (self.df.isnull().sum() / self.df.shape[0])))
        y = dict(zip(self.df.columns, x))
        return pd.DataFrame(y, index=['Number of Values', 'Data Type', 'Perc Null']).transpose()
    
    def skew_list(self):
        skew_list = self.df.skew().map(lambda x: abs(x)).sort_values(ascending=False).index
        if len(skew_list) > 3:
            skew_list = skew_list[:3]
        return skew_list

    
    def corr_list(self):
        c = self.df.corr().abs()
        s = c.unstack()
        so = s.sort_values(ascending=False)
        i = int(len(so) ** (1/2))
        charts = so[i:]
        charts = charts[::2]
        if len(charts) > 3:
            charts = charts[:3]
        return charts.index, charts.values
    
    
    def describe(self):
        return self.df.describe().transpose()