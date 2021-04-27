import pyodbc
import pandas as p

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\manvendra.1.s\Documents\Test.accdb;')

SQL_query = p.read_sql_query('select Username, City from UserData', conn)

df = p.DataFrame(SQL_query)
df.to_csv('Output.csv', index=False)
