import sqlite3

conn = sqlite3.connect('../data/WaterFP.sqlite')
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
    """)



