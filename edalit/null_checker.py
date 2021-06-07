class Null:
    
    def __init__(self, df) -> None:
        self.df = df
    
    def nulls(self):
        return self.df.isnull().sum() / self.df.shape[0]
    
    def drop(self, cols: list):
        return self.df.drop(columns=cols)
    
    def impute(self, cols: list, methods: list):
        dic = dict(zip(cols, methods))

        for i in dic:
            if dic[i] == 'mode':
                dic[i] = self.df[i].mode(dropna=True)[0]
            elif dic[i] == 'mean':
                dic[i] = self.df[i].mean()
            else:
                dic[i] = self.df[i].median()
                
        return self.df.fillna(dic)