import pandas as pd


class Information:
    """Class used to get useful information from dataframe used in the apps.
    """
    
    def __init__(self, df) -> None:
        self.df = df
        
    def information(self):
        """Used to return simple information from dataframe passed to the class

        Returns:
            pandas dataframe: Dataframe with information about the count of values in the data, data types, and percent of 
            missing data
        """
        
        
        x = list(zip(self.df.count(), self.df.dtypes, (self.df.isnull().sum() / self.df.shape[0])))
        y = dict(zip(self.df.columns, x))
        return pd.DataFrame(y, index=['Number of Values', 'Data Type', 'Percent Missing']).transpose()
    
    def skew_list(self):
        """Used to return a list of columns from dataframe passed to class. List is ordered in 
        descending order with respect to the skew of the data in the columns.

        Returns:
            list: top three columns in data with highest skew
        """
        skew_list = self.df.skew().map(lambda x: abs(x)).sort_values(ascending=False).index
        if len(skew_list) > 3:
            skew_list = skew_list[:3]
        return skew_list

    
    def corr_list(self):
        """Used to return list of tuples of dataframe columns. Ordered in descending order with respect
        to the correlation between the pairs of columns

        Returns:
            list: list of top three pairs of columns with the highest correlation --> [(a,b)...(e,f)]
        """
        c = self.df.corr().abs()
        s = c.unstack()
        so = s.sort_values(ascending=False)
        i = int(len(so) ** (1/2))
        charts = so[i:]
        charts = charts[::2]
        if len(charts) > 3:
            charts = charts[:3]
        return charts.index, charts.values
