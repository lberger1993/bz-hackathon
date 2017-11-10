import sqlite3

conn = sqlite3.connect('../data/WaterFP.sqlite')
cur = conn.cursor()

cur.executescript("""
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Chocolate', '17,196');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Beef', '15,415');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Sheep Meat ', '10,412');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Pork', '5,988');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Butter', '5,553');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('chicken meat', '4,325');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('cheese', '3,178');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('olives', '3,025');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('rice', '2,497');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('cotton', '2,495');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Pasta (dry) ', '1,849'); 
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Bread', '1,608');
    """)



