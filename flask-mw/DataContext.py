import sqlite3
import json

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'WaterFP.sqlite')

conn = sqlite3.connect(db_path, check_same_thread=False)
cur = conn.cursor()


def get_product_list():
    db_data = cur.execute("SELECT * FROM FoodItems").fetchall()
    product_list = []
    for prod in db_data:
        json_item = json.loads('{"id" : %d, "ProductName" : "%s", "WaterCost" : %s}' % (prod[0], prod[1], prod[2]))
        product_list.append(json_item)
    return json.dumps(product_list)


def get_all_recipies():
    result=[]
    all_rec_ids= cur.execute("SELECT ID FROM RECIPIES").fetchall()
    for id in all_rec_ids:
        result.append(get_recipe(id[0]))
    return json.dumps(result)

def get_recipe(recipeID):
    db_rec = cur.execute("SELECT * FROM RECIPIES WHERE ID = ?", (str(recipeID),)).fetchone()
    if db_rec is None:
        res = json.loads('{"Message" : "Data Not Found"}')
        return res
    json_str = "{{\"RecipeID\" : {:d}, \"RecipeName\" : \"{}\"".format(db_rec[0], db_rec[1])
    query = '''SELECT f.ID, f.FoodItemName, f.WaterPerKilo, r.AmountInKilo, f.AlternativeFoodItem, f.AlternativeWaterPerKilo FROM FoodItems AS f INNER JOIN RecipeItems AS r on f.ID=r.FoodItemID WHERE r.RecipeID = {:d}'''.format(
        db_rec[0])
    db_fooditems = cur.execute(query).fetchall()
    foodItems=[]
    if len(db_fooditems)>0:
        json_str+=',"FoodItems" : ['
        for item in db_fooditems:
            curr_str='{"FoodIemID" : %d, "ProductName" : "%s", "WaterPerKilo" : %d, "AmountInRecipe" : %s,  "Alternative" : "%s", "AlternativeAmountInRecipe": "%s"  }'\
                     %(item[0], item[1], item[2], str(item[3]), item[4], item[5])
            foodItems.append(curr_str)
        food_items_str = ",".join(foodItems)
        json_str+=food_items_str
        json_str += "]"
    json_str += "}"
    res=json_str
    return json.loads(res, strict=False)

def get_load_recipes_partners_tables():
    db_data = cur.execute("SELECT * FROM RecipePartners").fetchall()
    return_list = []
    for val in db_data:
        json_item = json.loads('{"id" : %d, "bad_recipe" : "%s", "good_recipe" : %s}' % (val[0], val[1], val[2]))
        return_list.append(json_item)
    return json.dumps(return_list)


def data_calculate_water_score(data_body):
    id_list = [item['id'] for item in data_body]
    id_string = ','.join(str(x) for x in id_list)
    id_string = '(' + id_string + ')'
    db_data = cur.execute("SELECT * FROM FoodItems WHERE id in %s" % (id_string)).fetchall()
    response_body = {'total_water': 0, 'data_body': []}
    for data_point in db_data:
        for val in data_body:
            if data_point[0] == val.get('id'):
                new_response = {}
                new_response['individual_sum'] = int(val.get('quantity')) * data_point[2]
                response_body['total_water'] = response_body['total_water'] + new_response['individual_sum']
                new_response['id'] = data_point[0]
                new_response['ingredient'] = data_point[1]
                response_body.get('data_body').append(new_response)
    return json.dumps(response_body)




