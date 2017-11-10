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

def get_all_recipies():
    result=[]
    all_rec_ids=cur.execute("SELECT ID FROM RECIPIES").fetchall()
    for id in all_rec_ids:
        print(id[0])
        result.append(get_recipe(id[0]))
    return result

def get_recipe(recipeID):
    db_rec = cur.execute("SELECT * FROM RECIPIES WHERE ID = ?", (str(recipeID),)).fetchone()
    if db_rec is None:
        res = json.loads('{"Messge" : "Data Not Found"}')
        return res
    json_str = "{{\"RecipeID\" : {:d}, \"RecipeName\" : \"{}\"".format(db_rec[0], db_rec[1])
    # print(db_rec[0])
    query = '''SELECT f.ID, f.FoodItemName, f.WaterPerKilo, r.AmountInKilo  FROM FoodItems AS f INNER JOIN RecipeItems AS r on f.ID=r.FoodItemID WHERE r.RecipeID = {:d}'''.format(
        db_rec[0])
    # print(query)
    db_fooditems = cur.execute(query).fetchall()
    foodItems=[]
    if len(db_fooditems)>0:
        json_str+=',"FoodItems" : ['
        for item in db_fooditems:
            #print(item)
            # print(item[3])
            curr_str='{"FoodIemID" : %d, "ProductName" : "%s", "WaterPerKilo" : %d, "AmountInRecipe" : %s }'%( item[0], item[1], item[2], str(item[3]))
            # print(curr_str)
            foodItems.append(curr_str)
            #json_str += '{"FoodIemID" : %d, "ProductName" : "%s", "WaterPerKilo" : %d, "AmountInRecipe" : %d},'%( item[0], item[1], item[2], item[3])
        food_items_str = ",".join(foodItems)
        json_str+=food_items_str
        json_str += ']'
    json_str += "}"

    # print(food_items_str)
    # print(json_str)
    res=json.loads(json_str)
    return res


if __name__ == '__main__':
    print(get_all_recipies()[1])




