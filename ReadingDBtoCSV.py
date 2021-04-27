import pyodbc
import pandas as p

# Connect Query for My Access DB
conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=<Location_of_MSAcess>\Test.accdb;')

# Connection Query for Oracle
# import cx_Oracle
# con = cx_Oracle.connect('username/password@<HOST>')

SQL_query = p.read_sql_query('select Username, City from UserData', conn)

df = p.DataFrame(SQL_query)
df.to_csv('Output.csv', index=False)
