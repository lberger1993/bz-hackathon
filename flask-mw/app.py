from flask import Flask, send_file
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

#
# class GetInitalRecipes(Resource):
#     def get(self):
#         # return
#         {recipe_list: [{
#                 recipe_name:
#
#         }]}

@app.route("/")
def index():
    return send_file("templates/index.html")





# api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)