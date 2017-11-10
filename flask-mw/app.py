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
    print(request.data)

# def reedem_points_for_local_purchases():

if __name__ == '__main__':
    app.run(debug=True)