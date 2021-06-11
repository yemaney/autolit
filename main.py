import streamlit as st
from edalit.file_importer import File
from edalit.data_reader import Information

section = st.sidebar.selectbox('Section', ('Home', 'File Upload', 'Plot'))


if section == 'Home':
    st.title('Edalit')
    
    st.write('Streamlining explanatory data analysis of tabular information, and wrapping it in a streamlit app.')
    
elif section == 'File Upload':
    st.title('Upload Data to Explore')
    
    upload = st.file_uploader(label='File Here')
    
    if upload is not None:
        file = File(upload)
        file = file.import_csv(',')
        file
        
        info = Information(file)
        
         
        i = info.information()
        i
        c = info.corr()
        c
        d = info.describe()
        d 
        

elif section == 'Plot':
    pass