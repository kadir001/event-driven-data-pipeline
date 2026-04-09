import logging
import os

from src.extract import extract
from src.transform import transform
from src.load import load
from src.analyze import analyze
from config import LOG_PATH

# Zorg dat logs folder bestaat
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    try:
        logging.info("Pipeline gestart")

        df = extract()
        df = transform(df)
        load(df)

        result = analyze()
        print(result.to_string())

        logging.info("Pipeline succesvol afgerond")

    except Exception as e:
        logging.error(f"Fout in pipeline: {e}")
        raise
