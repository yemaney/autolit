import altair as alt


class Plotter:
    
    def __init__(self, df) -> None:
        self.df = df
        
    def corr_plotter(self, corr_labels: list):
        charts =[]
        for  labels in corr_labels:
            chart = alt.Chart(self.df).mark_point().encode(
                x=labels[0],
                y=labels[1]
            )
            
            charts.append(chart)
        
        return charts
    
    def skew_plotter(self, skew_labels: list):
        charts = []
        for  label in skew_labels:
            chart = alt.Chart(self.df).mark_bar().encode(
                x= alt.X(label, bin=True),
                y= 'count()'
            )
            
            charts.append(chart)
        
        return charts     