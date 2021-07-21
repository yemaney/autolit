import streamlit as st
import streamlit.components.v1 as components
from autolit.file_importer import File
from autolit.data_reader import Information
from autolit.alt_plotter import ALT_Plots
from autolit.slide import SlideShow
from autolit.sns_plotter import SNS_Plots

from sklearn.utils import estimator_html_repr

import seaborn as sns
sns.set_theme()

from autolit.autopipe import Autopipe
from autolit.lr_plot import plot_learning_curve

section = st.sidebar.selectbox('Section', ('Home', 'Upload Data', 'Explore Data', 'Modeling'))


if section == 'Home':
    st.title('Autolit')
    
    st.write('''
            Streamlining explanatory data analysis and machine-learning of tabular information, and wrapping it in a streamlit app.
            
            ---
            ### Work flow of app
            - Upload Data
            - Choose where to get your data.
            - Confirm file type and import
            - Explore Data
            - Observe interesting plots and basic data descriptions
            - Modeling
            - Construct pipeline to predict on data
            ---            
             ''')
    
    image = 'https://images.unsplash.com/photo-1543286386-713bdd548da4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80'
    st.image(image, 'Data is Interesting')
elif section == 'Upload Data':
    st.write('''
            How to upload:
            - Choose where to get your data. Either upload your own, use link, or default loan data
            - Confirm the data type (csv or xls)
            - Import the data''')
    with st.form('Data chooser'):
        import_choice = st.selectbox(label='Choose where to get your data.', options=('Loan_Data', 'Upload', 'Link'))
        if import_choice == 'Loan_Data':
            upload = 'data/data.csv'
        elif import_choice == 'Upload':
            upload = st.file_uploader(label='File Here')
        else:
            upload = st.text_input(label='enter link here')
        choose_submit = st.form_submit_button('Choose data')
        if choose_submit:
            st.session_state.DATA = upload   
    
    
    if 'DATA' not in st.session_state:
        st.title('Upload Data to Explore')
    else:
        file_type = st.selectbox(label='filetype', options=('csv', 'xls'))
        if file_type == 'csv':
            with st.form('Import csv'):
                st.subheader('Import csv file here')
                file = File(st.session_state.DATA)
                sep = st.selectbox('seperator', (',', ';', '    '), help='blank selection is for tab seperated sheets.')
                csv_submitted = st.form_submit_button('Import csv')
                if csv_submitted:
                    file = file.import_csv(sep)
                    st.session_state.df = file
                    file
                    
        elif file_type == 'xls':   
            with st.form('Import xls'):
                st.subheader('Import xls file here')
                file = File(st.session_state.DATA)
                sheetnames = file.xls_sheets()
                sheetname = st.selectbox('sheetname', (sheetnames), help='Choose which excel sheet to use data from.')
                xls_submitted = st.form_submit_button('Import xls')
                if xls_submitted:
                    file = file.import_xls(sheetname)
                    st.session_state.df = file
                    file
                    

elif section == 'Explore Data':
    if 'df' not in st.session_state:
        st.title('Upload Data to Explore')
    else:
        st.title('Autogenerated plots')
        st.write('''
                - Distribution plots are displayed in descending order, with respect to their skew.
                - Correlation plots are displayed in descending order, with respect to their correlation.
                
                ---''')
        df = st.session_state.df
        if len(df) > 5000:
            df = st.session_state.df.sample(5000, random_state=0)
        info = Information(df)
        st.header('Data Types')
        st.dataframe(info.information()['Data Type'].reset_index().rename(columns={'index':'variable'}).transpose())
        
        skew_list = info.skew_list()
        corr_list, _ = info.corr_list()

        plotter = ALT_Plots(df)
        skew_plots = plotter.skew_plotter(skew_list)
        corr_plots = plotter.corr_plotter(corr_list)
        info_plots = plotter.info_plotter(info.information())

        html = open('src/slide.html', 'r').read()
        css = open('src/style.css', 'r').read()
        js = open('src/script.js', 'r').read()

        skew_sl = SlideShow(skew_plots, html, css, js)
        skew_sl = skew_sl.create()
        corr_sl = SlideShow(corr_plots, html, css, js)
        corr_sl = corr_sl.create()
        info_sl = SlideShow(info_plots, html, css, js)
        info_sl = info_sl.create()
        
        st.header('Distribution Plots')
        components.html(skew_sl, height=400,scrolling=True)
        st.write('---')
        st.header('Correlation Plots')
        components.html(corr_sl, height=400,scrolling=True)
        st.write('---') 
        st.header('General Information')
        st.markdown('''
                    This is information about
                    - Percent of missing values
                    - Number of values''')
        components.html(info_sl, height=500,scrolling=True) 
        st.write('---')


        snsplots = SNS_Plots(df)


        st.header('Correlation Matrix')
        st.markdown('''Standard pearson correlation between numerical variables''')
        heatmap = snsplots.heatmap()
        st.pyplot(heatmap)
        # f = open('test.html', 'w')
        # f.write(corr_sl)
        # f.close()      
        st.write('---')  
        st.markdown('''
                    These forms allow for more plot viewing. 
                    - Displays plots in groups of 9 or less
                    - Useless columns such as ID** may make countplot loading long''')
        st.header('Optional Boxplot examiner')
        snsplots.boxplots()
        st.header('Optional Countplot examiner')
        snsplots.countplots()
elif section == 'Modeling':
    if 'df' not in st.session_state:
        st.title('Upload Data to Explore')
        
    else:
        st.title('Modeling the Data')

        st.markdown('---')
        with st.form('Contruct Pipeline'):
            st.header('Contruct Pipeline')
            
            df = st.session_state.df
            y = st.selectbox(label='Pick Target Variable', options=df.columns)
            
            if st.form_submit_button(label='Start the pipeline'):
                with st.spinner(text='Contructing Pipeline'):   
                    pipe = Autopipe(df, y)
                    grid_search, X_test, y_test = pipe.clf_pipelin()
                    
                    st.header('Most importan features')
                    X = df.drop(columns=[y])
                    sup = grid_search.best_estimator_.named_steps['selector'].get_support()
                    features = X[X.columns[sup]]
                    st.dataframe(features)
                    
                    st.header('Best Pipeline')
                    components.html(estimator_html_repr(grid_search.best_estimator_), scrolling=True, height=200)
                    st.code(grid_search.best_estimator_)
                    st.header('Best Score')
                    st.code(grid_search.best_score_)
                    
                    st.header('Learning Curve Plots')
                    X = df.drop(columns=[y])
                    
                    lr = plot_learning_curve(grid_search.best_estimator_, 'Pipline Learngin Curve', X_test, y_test)
                    
                    st.pyplot(lr)