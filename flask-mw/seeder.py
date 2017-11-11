import sqlite3

conn = sqlite3.connect('../data/WaterFP.sqlite')
cur = conn.cursor()


# coffee
# 18900
# Beef beef
# 15400
# Sheep sheep
# 10400
# Pork pork
# 6000
# Goat goat
# 5500
# Chicken chicken
# 4300
# Cheese cheese
# 3180
# Rice rice
# 2500
# Soyabeans soyabeans
# 2145
# Wheat wheat
# 1830
# Sugar sugar
# 1780
# Barley barley
# 1425
# Maize maize
# 1220
# Apple apple
# 822
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
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Bread', '1608');
    insert into FoodItems (FoodItemName, WaterPerKilo) values ('Bread', '1608');
    """)
    # appropriate &

