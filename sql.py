import sqlite3
connection = sqlite3.connect("ResumeShortlist.db")
cursor = connection.cursor()

table_info1="""
Create table Job(Id INTEGER PRIMARY KEY   AUTOINCREMENT,JobName varhar(25),JobDescription varchar(25));
"""
cursor.execute(table_info1)
table_info2="""
Create table JobResume(Id INTEGER PRIMARY KEY   AUTOINCREMENT,JobId int,ResumeId int, ScoreId int, MatchComments varchar(25));
"""
cursor.execute(table_info2)

table_info3="""
Create table Resume(Id INTEGER PRIMARY KEY   AUTOINCREMENT,CandidateName varchar(25),CandidateSkills varchar(25));
"""
cursor.execute(table_info3)
##insert records.
cursor.execute(''' Insert into Job values(NULL,'Job1','.Net Full Stack') ''')
cursor.execute(''' Insert into Job values(NULL,'Job2','java Full Stack') ''')
cursor.execute(''' Insert into Job values(NULL,'Job3','servicenow Full Stack') ''')
cursor.execute(''' Insert into JobResume values(NULL,1,1,0.85,'good  match') ''')
cursor.execute(''' Insert into JobResume values(NULL,2,1,0.12,'poor  match') ''')
cursor.execute(''' Insert into JobResume values(NULL,3,1,0.45,'average  match') ''')
data= cursor.execute(''' select * from Job ''')
for row in data:
    print (row)
data1= cursor.execute(''' select * from JobResume ''')
for row in data1:
    print (row)
cursor.close()
connection.commit()
connection.close()