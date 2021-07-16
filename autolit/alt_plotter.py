import altair as alt

class ALT_Plots:
    """A class used to handle all the altair plots in this 
    streamlit app

    Args:
        df (pandas dataframe): Dataframe from which plots will be generated from.
    """
    
    def __init__(self, df) -> None:
        self.df = df
        
    def corr_plotter(self, corr_labels: list):
        """Used to create a list of altair scatterplot chart objects

        Args:
            corr_labels (list): list of tuples of dataframe columns that have numeric data types

        Returns:
            [list]: [list of altair scatter plot charts]
        """
        
        
        charts =[]
        for  labels in corr_labels:
            chart = alt.Chart(self.df).mark_point().encode(
                x=labels[0],
                y=labels[1]
            )
            
            charts.append(chart)
        
        return charts
    
    def skew_plotter(self, skew_labels: list):
        """Used to create a list of altair histogram chart objects

        Args:
            skew_labels (list): list of dataframe columns that have numeric data types

        Returns:
            [list]: list of altair histogram plot charts
        """        
        
        
        charts = []
        for  label in skew_labels:
            chart = alt.Chart(self.df).mark_bar().encode(
                x= alt.X(label, bin=True),
                y= 'count()'
            )
            
            charts.append(chart)
        
        return charts
    
    
    @staticmethod
    def info_plotter(df):
        """Used to create a list of altair bar chart objects. With information
        about the count and missing of values in the dataframe.

        Args:
            df ([pandas dataframe]): dataframe then went through info = Information(df).information()

        Returns:
            [list]: list of altair bar plot charts
        """
        
        
        
        charts = []
        
        df = df.reset_index().rename(columns={'index': 'variables'})
        null_df = df[['variables', 'Percent Missing']]
        count_df = df[['variables', 'Number of Values']]
        
        null_charts = alt.Chart(null_df).mark_bar().encode(
            x='variables:O',
            y='Perc Null:Q'
        )
        
        charts.append(null_charts)
        
        count_charts = alt.Chart(count_df).mark_bar().encode(
            x='variables:O',
            y='Number of Values:Q'
        )
        charts.append(count_charts)
        return charts