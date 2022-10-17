import pyodbc
import pandas as pd
import os
from datetime import datetime
from plyer import notification

#create SQL conneciton

# connection = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; server=localhost; host='JOEL-LAPTOP\SQLEXPRESS', db='SalesOrder',
#                             Trusted_Connection='no'")
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=JOEL-LAPTOP\SQLEXPRESS;'
    r'DATABASE=DepartmentDb;'
    r'Trusted_Connection=yes;'
)
cnxn = pyodbc.connect(conn_str)

# connection = pyodbc.connect(
#     'DRIVER={JOEL-LAPTOP\SQLEXPRESS}; host="JOEL-LAPTOP\SQLEXPRESS"; db=SalesOrder')

# Read data from SQLEXPRESS
sqlQuery = "SELECT City, FirstName, LastName FROM [DepartmentDb].[dbo].[Staff] where City='Johannesburg'"

df = pd.read_sql_query(sql=sqlQuery, con=cnxn)

print(df)
#export the data to a specific location

df.to_csv(os.environ['userprofile'] +
          "\\Documents\Github\python_sql_automation\exported_data\\" + "Department" + datetime.now().strftime("%d-%b-%m-%y %H:%M"))
# print(df['FirstName'])

#Notify the user
# 467 George Road, Noordwyk Midrand
notification.notify(title="Report status!!!",
                    message=f"The department staff details have been successfully exported to a csv file. \n Total Rows: {df.shape[0]}\n Total Columns: {df.shape[1]}\n")
