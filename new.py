import pandas as pd
import os

data = {
    "ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Join_Date": pd.to_datetime(["2026-01-10", "2026-01-15", "2026-02-01", "2026-02-05"]),
    "Score": [85, 90, 78, 92]
}

df=pd.DataFrame(data)

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample.csv')

df.to_csv(file_path,index=False)