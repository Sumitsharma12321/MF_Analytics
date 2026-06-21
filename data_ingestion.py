import pandas as pd
import os

data_path = "data/raw"

print("\nDataset Summary")
print("-" * 70)

for file in os.listdir(data_path):

    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(data_path, file))

        print(
            f"{file:25} | Rows: {df.shape[0]:5} | Cols: {df.shape[1]} | Missing: {df.isnull().sum().sum()}"
        )