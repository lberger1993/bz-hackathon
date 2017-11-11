import sqlite3

conn = sqlite3.connect('../data/WaterFP.sqlite')
cur = conn.cursor()

cur.executescript("""
    DELETE FROM FoodItems;
""")