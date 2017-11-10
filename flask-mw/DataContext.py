import sqlite3
import json

conn = sqlite3.connect('../data/WaterFP.sqlite')
cur = conn.cursor()


def get_product_list():
    db_data = cur.execute("SELECT * FROM FoodItems").fetchall()
    product_list = []
    for prod in db_data:
        json_item = json.loads('{"id" : %d, "ProductName" : "%s", "WaterCost" : %s}' % (prod[0], prod[1], prod[2]))
        product_list.append(json_item)
    return product_list


def get_recipe(recipeID):
    db_rec = cur.execute("SELECT * FROM RECIPIES WHERE ID = ?", (str(recipeID),)).fetchone()
    if db_rec is None:
        res = json.loads('{"Messge" : "Data Not Found"}')
        return res
    json_str = "{{\"RecipeID\" : {:d}, \"RecipeName\" : \"{}\"".format(db_rec[0], db_rec[1])
    print(db_rec[0])
    query = "SELECT FoodItems.ID, FoodItems.FoodItemName, FoodItems.WaterPerKilo, RecipeItems.AmountInKilo  " \
            "FROM FoodItems INNER JOIN RecipeItems on FoodItems.ID=RecipeItems.FoodItemID WHERE RecipeID = {:d}".format(
        db_rec[0])
    print(query)
    db_fooditems = cur.execute(query).fetchall()
    print(db_fooditems)
    for fd_item in db_fooditems:
        print(fd_item)

    return ''


if __name__ == '__main__':
    res = get_recipe(1)
    print(res)
