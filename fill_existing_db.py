import sqlite3 as sq
import pandas as pd
from pathlib import Path
from shutil import rmtree

db_files = "db_data"
tables = ["Accounts","Customers","Suppliers","Journals","Invoice_Payments","Bill_Payments","Received_Moneys","Spent_Moneys","Received_Money_Lines","Spent_Money_Lines","Invoices","Invoice_Lines","Bills","Bill_Lines"]

# select database name here
conn = sq.connect("accounting_db.db")
curs = conn.cursor()

for table_name in tables:
    df = pd.read_csv(f"{db_files}/{table_name}.csv")
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    curs.execute(f"select count(*) from {table_name}")
    records = curs.fetchall()
    print(f"{table_name}: ", records[0][0], " records")

conn.close()