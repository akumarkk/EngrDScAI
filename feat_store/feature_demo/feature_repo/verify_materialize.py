import sqlite3

# Connect to your online store database
conn = sqlite3.connect("data/online_store.db")
cursor = conn.cursor()

# Query the materialized feature table
cursor.execute("SELECT * FROM feature_demo_driver_hourly_stats LIMIT 3;")
print("Materialized rows:", cursor.fetchall())

conn.close()