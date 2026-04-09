import pandas as pd
import logging
from src.utils import get_last_timestamp


def transform(df):
    logging.info("Start transform fase")

    df = df.dropna(subset=["user_id"]).copy()
    df["device"] = df["device"].fillna("unknown")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.drop_duplicates().copy()

    last_ts = get_last_timestamp()

    if last_ts:
        logging.info(f"Laatste timestamp in DB: {last_ts}")
        df = df[df["timestamp"] > last_ts]

    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.day_name()
    df["is_weekend"] = df["day_of_week"].isin(["Saturday", "Sunday"])

    logging.info(f"Aantal rijen na transform: {len(df)}")

    return df
