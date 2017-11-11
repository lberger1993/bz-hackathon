from flask import Flask, send_file, request
from DataContext import *
import qrcode

app = Flask(__name__)


# app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return send_file("templates/index.html")


@app.route("/api/v1/get_all_food", methods=['GET'])
def return_all_foods():
    return get_product_list()


@app.route("/api/v1/get_all_recipes", methods=['GET'])
def return_all_recipes():
    return get_all_recipies()


@app.route("/api/v1/calculate_water_score", methods=["POST"])
def calculate_water_score():
    data_body = json.loads(request.form.get('data'))
    return data_calculate_water_score(data_body)


# @app.route('/api/v1/get_recipe_partners', methods=['GET'])
# def return_recipe_partners():
#     return get_load_recipes_partners_tables()


@app.route('/api/v1/get_qr_code', methods=['POST'])
def get_qr_code():
    recipe_id = int(request.form.get('receipe_id'))
    recipe = get_recipe(recipe_id)
    qrText = str(recipe["RecipeID"]) + ' ' + recipe["RecipeName"]
    qr_img = qrcode.make(qrText)
    qr_img.show()

    return qr_img


if __name__ == '__main__':
    app.run(debug=True)
