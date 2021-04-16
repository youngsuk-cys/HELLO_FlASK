from flask import Flask
from flask_restful import Resource , Api 
from src.base.Controller import *
app = Flask(__name__)
# app.config["DEBUG"] = True

api = Api(app)


api.add_resource(RegistUser, '/user')
api.add_resource(User , '/aa')

@app.route("/")
def home():
    return "Flask API Test Server !!!"

if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0',port='8888')



