import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
import pandas as pd


class SNS_Plots():
    """A class used to handle all the seaborn plots in this 
    streamlit app

    Args:
        df (pandas dataframe): Dataframe from which plots will be generated from.
    """
    
    def __init__(self, df) -> None:
        self.df = df
        
    
    def boxplots(self):
        """Used to create a streamlit form that produces boxplots.
        Boxplots are produced from the dataframe passed when the class
        was instantiated. Displays at most (9) plots at once. Can decide 
        which columns to plot through select-box.
        
        Returns:
            Streamlit form object that will show respective seaborn
            countplots upon submition
        """
        
        
        with st.form('boxplots'):
            num = self.df.select_dtypes('number')
            lst = num.columns.values
            if len(lst) < 9:
                sub = 1
            else:
                sub = (len(lst) // 9) + 1
            splits = np.array_split(lst, sub)
            labels = [f'Boxplots {i+1}' for i in range(len(splits))]
            selections = st.selectbox(label='Choose Data to Plot',options=labels)
            idx = labels.index(selections)
            box = splits[idx]
            st.write(box)
            if st.form_submit_button(label='submit'):        
                col1, col2, col3 = st.beta_columns(3)
                a = 0
                for i in range(len(box)):
                    if a == 0:
                        col = col1
                        a += 1
                    elif a == 1:
                        col = col2
                        a += 1
                    else:
                        col = col3
                        a -= 2
                    with col:
                        fig, ax = plt.subplots()

                        ax = sns.boxplot(data=num,
                                    x=num[box[i]])
                        st.pyplot(fig)
                        
    def countplots(self):
        """Used to create a streamlit form that produces boxplots.
        Boxplots are produced from the dataframe passed when the class
        was instantiated. Displays at most (9) plots at once. Can decide 
        which columns to plot through select-box.
        
        
        Returns:
            Streamlit form object that will show respective seaborn
            countplots upon submition
        """
        
        
        
        with st.form('countplots'):
            num = self.df.select_dtypes('object')
            lst = num.columns.values
            if len(lst) < 9:
                sub = 1
            else:
                sub = (len(lst) // 9) + 1
            splits = np.array_split(lst, sub)
            labels = [f'Countplots {i+1}' for i in range(len(splits))]
            selections = st.selectbox(label='Choose Data to Plot',options=labels)
            idx = labels.index(selections)
            box = splits[idx]
            st.write(box)
            if st.form_submit_button(label='submit'):        
                col1, col2, col3 = st.beta_columns(3)
                a = 0
                for i in range(len(box)):
                    if a == 0:
                        col = col1
                        a += 1
                    elif a == 1:
                        col = col2
                        a += 1
                    else:
                        col = col3
                        a -= 2
                    with col:
                        fig, ax = plt.subplots()

                        ax = sns.countplot(data=num,
                                    x=num[box[i]])
                        st.pyplot(fig)
                        

    def heatmap(self):
        """Method to create seaborn heatmap for the correlation matrix
        of the numerical variable from the dataframe passed to class

        Returns:
            seaborn plot: A heatmap of the pearson correlation between df
            numerical values
        """
        
        
        heatmap = self.df.corr()
        fig, ax = plt.subplots()
        ax = sns.heatmap(heatmap, cmap="YlGnBu")
        return fig        
    
    

class Feature_Importance: 
    
    def __init__(self) -> None:
        pass
        
    def plot(self, X: pd.DataFrame, scores):
        dic = {}
        for x, y in zip(X.columns, scores):
            dic[x] = y
            
        df_scores = pd.DataFrame.from_dict(dic, orient='index').transpose()
        
        fig, ax = plt.subplots()
        ax = sns.barplot(data=df_scores)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
        plt.tight_layout()
        
        return fig