import sqlite3
import json

from flask import Flask, send_file, request

app = Flask(__name__)

conn = sqlite3.connect('../data/WaterFP.sqlite', check_same_thread=False)
cur = conn.cursor()


@app.route("/")
def index():
    return send_file("templates/index.html")


@app.route("/api/v1/get_all_food", methods=['GET'])
def return_all_foods():
    db_data = cur.execute("SELECT * FROM FoodItems").fetchall()
    product_list = []
    for prod in db_data:
        json_item = json.loads('{"id" : %d, "ProductName" : "%s", "WaterCost" : %s}' % (prod[0], prod[1], prod[2]))
        product_list.append(json_item)

    print(product_list)
    return json.dumps(product_list)


@app.route("/api/v1/get_all_recipes", methods=['GET'])
def return_all_recipes():
    db_data = cur.execute("SELECT * FROM Recipies").fetchall()
    product_list = []
    for prod in db_data:
        json_item = json.loads('{"id" : %d, "RecipieName" : "%s"}' % (prod[0], prod[1]))
        product_list.append(json_item)
    return json.dumps(product_list)


@app.route("/api/v1/calculate_water_score", methods=["POST"])
def calculate_water_score():
    data_body = json.loads(request.form.get('data'))
    id_list = [item['id'] for item in data_body]
    id_string = ','.join(str(x) for x in id_list)
    id_string = '(' + id_string + ')'
    db_data = cur.execute("SELECT * FROM FoodItems WHERE id in %s" % (id_string)).fetchall()
    response_body = {'total_water': 0, 'data_body': []}
    for data_point in db_data:
        for val in data_body:
            if data_point[0] == val.get('id'):
                new_response = {}
                new_response['individual_sum']= int(val.get('quantity'))*data_point[2]
                response_body['total_water'] = response_body['total_water'] + new_response['individual_sum']
                new_response['id'] = data_point[0]
                new_response['ingredient'] = data_point[1]
                response_body.get('data_body').append(new_response)
    return json.dumps(response_body)

if __name__ == '__main__':
    app.run(debug=True)