# event-driven-data-pipeline
End-to-end data engineering pipeline with ETL, incremental loading, logging, and modular architecture using Python and SQLite.

This project is an end-to-end data engineering pipeline built with Python.

## 🚀 Features
- Extract data from multiple CSV files
- Data cleaning and transformation
- Incremental loading (only new data processed)
- SQLite database storage
- SQL-based analysis
- Logging system
- Modular pipeline structure

## 🧱 Project Structure
.
├── data/
│   ├── raw/
│   └── processed/
├── logs/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── analyze.py
│   └── utils.py
├── config.py
├── pipeline.py
└── README.md

## ⚙️ How to Run

```bash
pip install pandas
python3 pipeline.py

📊 Example Output
device   total_events
desktop  2
mobile   2
unknown  2

🧠 Concepts Used
ETL (Extract, Transform, Load)
Incremental processing
Logging
Modular architecture
SQL analysis
