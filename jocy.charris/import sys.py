import sys

import pyodbc

conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cuc\Documents\Software\bdprueba.accdb;")
cursor=conn.cursor()

cursor.execute("SELECT * FROM persona")

for row in cursor.fetchall():
    print()
cursor.close
def jls_extract_def():
    
    return 


conn.close = jls_extract_def()

