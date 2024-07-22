import sqlite3
connection = sqlite3.connect("ResumeShortlist.db")
cursor = connection.cursor()
data= cursor.execute(''' select * from Job ''')
for row in data:
    print (row)
cursor.close()
connection.commit()
connection.close()