import requests
import pandas as pd
import os

# Create raw folder if not exists
os.makedirs("data/raw", exist_ok=True)

scheme_codes = {
    "hdfc_top_100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = f"data/raw/{fund_name}.csv"

        nav_df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    else:
        print(f"Failed for {fund_name}")