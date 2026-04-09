import os
import sqlite3
import pandas as pd
from config import DB_PATH


def get_last_timestamp():
    if not os.path.exists(DB_PATH):
        return None

    conn = sqlite3.connect(DB_PATH)

    query = "SELECT MAX(timestamp) as max_ts FROM events"
    result = pd.read_sql(query, conn)

    conn.close()

    return result["max_ts"][0]
