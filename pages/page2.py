from navigation import make_sidebar
import streamlit as st
from pathlib import Path
import sqlite3
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
make_sidebar()

st.write("Enter Details to create new job")
jobname = st.text_input("JobName")
jobDescription = st.text_area("JobDescription")
st.write("Please select Resumes")
File = st.file_uploader(label = "Upload file", type=["pdf","docx"])
submit= st.button("Save Job")
def insert_job_details(jobname,jobdescription,db):
    conn=sqlite3.connect(db)
    sql = "Insert into Job(id,JobName,JobDescription) values (NULL,?,?)"
    val= (jobname,jobdescription)
    cur= conn.cursor()
    cur.execute(sql,val)    
    conn.commit()
    conn.close()    
    return "rows"
def get_gemini_response(question,prompt):
    model= genai.GenerativeModel('gemini-pro')
    response= model.generate_content([prompt[0],question])
    return response.text
if submit:
    if File is not None:
        st.markdown("**The file is sucessfully Uploaded.**")
        # Save uploaded file to 'F:/tmp' folder.
        save_folder = 'C:\\genaiprojects\\Data\\UploadedFiles'
        save_path = Path(save_folder, File.name)
        with open(save_path, mode='wb') as w:
            w.write(File.getvalue())

        if save_path.exists():
            st.success(f'File {File.name} is successfully saved!')
            response= insert_job_details(jobname,jobDescription,"ResumeShortlist.db")
            response=get_gemini_response(question,prompt)
            ##todo 
            ##insert into resume
            ## call gen ai api to get score against job desc
            ## insert  score in jobresume
            print (response)