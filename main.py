import streamlit as st
from autolit.file_importer import File
from autolit.data_reader import Information
from autolit import SessionState
import pandas as pd

session_state = SessionState.get(DATA=None)


section = st.sidebar.selectbox('Section', ('Home', 'Explore Data'))


if section == 'Home':
    st.title('Autolit')
    
    st.write('''
             Streamlining explanatory data analysis and machine-learning of tabular information, and wrapping it in a streamlit app.
             
             Upload a csv or xls file below, before going through the modules below in the sidebar.
             ''')
    
    upload = st.file_uploader(label='File Here')
    session_state.DATA = upload

    image = 'https://images.unsplash.com/photo-1543286386-713bdd548da4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80'
    st.image(image, 'Data is Interesting')
elif section == 'Explore Data':
    st.title('Upload Data to Explore')
    
    if session_state.DATA is not None:
        col1, col2 = st.beta_columns(2)
        with col1:
            with st.form('Import csv'):
                st.subheader('Import csv file here')
                file = File(session_state.DATA)
                sep = st.selectbox('seperator', (',', ';', '    '), help='blank selection is for tab seperated sheets.')
                submitted = st.form_submit_button('Submit')
                if submitted:
                    file = file.import_csv(sep)
        with col2:
            with st.form('Import xls'):
                st.subheader('Import xls file here')
                file = File(session_state.DATA)
                sheetnames = file.xls_sheets()
                sheetname = st.selectbox('sheetname', (sheetnames), help='Choose which excel sheet to use data from.')
                submitted = st.form_submit_button('Submit')
                if submitted:
                    file = file.import_xls(sheetname)
                    

        if type(file) == pd.DataFrame:
            file
            
            IF = Information(file)
            info = IF.information()
            info
            desc = IF.describe()
            desc