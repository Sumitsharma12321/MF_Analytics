import pandas as pd
import os
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database/bluestock_mf.db")

path = "data/processed"

for file in os.listdir(path):

    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(path, file))

        fund_name = file.replace(".csv", "")
        df["fund_name"] = fund_name

        df.rename(
            columns={
                "date": "nav_date"
            },
            inplace=True
        )

        df.to_sql(
            "fact_nav",
            engine,
            if_exists="append",
            index=False
        )

        print(f"Loaded {file}")