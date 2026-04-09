import pandas as pd
import os
import logging
from config import RAW_PATH


def extract():
    logging.info("Start extract fase")

    files = os.listdir(RAW_PATH)
    dfs = []

    for file in files:
        if file.endswith(".csv"):
            path = os.path.join(RAW_PATH, file)
            logging.info(f"Inlezen bestand: {file}")
            df = pd.read_csv(path)
            dfs.append(df)

    combined = pd.concat(dfs, ignore_index=True)
    logging.info(f"Aantal rijen na extract: {len(combined)}")

    return combined
