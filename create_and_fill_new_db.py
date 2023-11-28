import sqlite3 as sq
import pandas as pd
from pathlib import Path
from shutil import rmtree

db_files = "db_data"
tables = ["Accounts","Customers","Suppliers","Journals","Invoice_Payments","Bill_Payments","Received_Moneys","Spent_Moneys","Received_Money_Lines","Spent_Money_Lines","Invoices","Invoice_Lines","Bills","Bill_Lines"]

db_name = "accounting_db2.db"
db_path = Path(db_name)

if db_path.exists():
    db_path.unlink()

# if not exists, it will create and connect to db
conn = sq.connect(db_name)
curs = conn.cursor()

for table_name in tables:
    df = pd.read_csv(f"{db_files}/{table_name}.csv")
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    curs.execute(f"select count(*) from {table_name}")
    records = curs.fetchall()
    print(f"{table_name}: ", records[0][0], " records")

conn.close()