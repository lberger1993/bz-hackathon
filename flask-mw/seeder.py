import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'WaterFP.sqlite')
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.executescript("""
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Chocolate', '17196');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Beef', '15415');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Sheep Meat ', '10412');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Pork', '5988');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Butter', '5553');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('chicken meat', '4325');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('cheese', '3178');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('olives', '3025');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('rice', '2497');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('cotton', '2495');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Pasta (dry) ', '1849'); 
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Bread', '1608');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Apple', '822');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('maize', '822');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Barley', '1425');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Sugar', '1780');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('wheat', '1830');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('soyabeans', '2145');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('goat', '5500');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('pork', '6000');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('sheep', '6000');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('coffee', '18900');
    """)

