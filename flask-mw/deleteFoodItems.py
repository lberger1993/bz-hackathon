import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'WaterFP.sqlite')
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.executescript("""
    DELETE FROM FoodItems;
""")