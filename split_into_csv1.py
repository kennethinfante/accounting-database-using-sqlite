import pandas as pd
from pathlib import Path
from shutil import rmtree

db_files = "db_data"

for path in Path(db_files).glob("**/*"):
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        rmtree(path)

data = pd.read_excel('service_type_business.xlsx', sheet_name=None)

# loop through the dictionary and save csv
for sheet_name, df in data.items():
    df.to_csv(f'{db_files}/{sheet_name}.csv', index=False)