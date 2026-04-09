import sqlite3
import pandas as pd
import logging
from config import DB_PATH


def analyze():
    logging.info("Start analyse fase")

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT device, COUNT(*) as total_events
    FROM events
    GROUP BY device
    """

    result = pd.read_sql(query, conn)
    conn.close()

    logging.info("Analyse succesvol uitgevoerd")

    return result
