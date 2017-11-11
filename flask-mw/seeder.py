import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'WaterFP.sqlite')
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.executescript("""
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Chocolate', '17196', 'Milk Products', '1006' );
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Beef', '15415', 'Mushrooms', '250');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Sheep Meat ', '10412', 'Mushrooms', '250');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Pork', '5988', 'Carrots', '250');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Butter', '5553',  'Soya', '250');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('chicken meat', '4325', 'eggs', '183');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('cheese', '3178', 'Nutritional Yeast', '200');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('olives', '3025', 'none', 'none');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('rice', '2497', 'none', 'none');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('cotton', '2495', 'none', 'none');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Pasta (dry) ', '1849', 'none', 'none'); 
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Bread', '1608', 'none', 'none');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Apple', '822', 'none', 'none' );
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('maize', '822', 'none', 'none' );
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Barley', '1425', 'none', 'none');
    insert into FoodItems (FoodItemName, WaterPerKilo, AlternativeFoodItem, AlternativeWaterPerKilo) values ('Sugar', '1780', 'none', 'none');
   
    """)

