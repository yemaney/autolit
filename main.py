import streamlit as st
from autolit.file_importer import File
from autolit.data_reader import Information
from autolit import SessionState

session_state = SessionState.get(DATA=None)


section = st.sidebar.selectbox('Section', ('Home', 'File Upload'))


if section == 'Home':
    st.title('Autolit')
    
    st.write('Streamlining explanatory data analysis and machine-learning of tabular information, and wrapping it in a streamlit app.')
    
elif section == 'File Upload':
    st.title('Upload Data to Explore')
    
    upload = st.file_uploader(label='File Here')
    
    file = None
    if session_state.DATA is not None:
        file = session_state.DATA
        file
    if upload is not None:    
        file = File(upload)
        file = file.import_csv(',')
        file
        
    session_state.DATA = file

    if file is not None:
        IF = Information(file)
        info = IF.information()
        info
        corr = IF.corr()
        corr
        desc = IF.describe()
        desc