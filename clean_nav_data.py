import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"

os.makedirs(processed_path, exist_ok=True)

for file in os.listdir(raw_path):

    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(raw_path, file))

        # date convert
        df["date"] = pd.to_datetime(df["date"], dayfirst=True)

        # sort by date
        df = df.sort_values("date")

        # remove duplicates
        df = df.drop_duplicates()

        # keep only positive nav
        df = df[df["nav"] > 0]

        # forward fill
        df["nav"] = df["nav"].ffill()

        # save
        output_file = os.path.join(processed_path, file)
        df.to_csv(output_file, index=False)

        print(f"Cleaned: {file}")