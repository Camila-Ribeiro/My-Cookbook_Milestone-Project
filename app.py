import os
import requests
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists('env.py'):
    import env

""" ENVIROMENT VARIABLES """
app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.environ.get('SECRET_KEY')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

api_key = "7b98ae9af6fe4cc6b9a33b00e08db54d"


@app.route('/', methods=['GET'])
def index():
    r = requests.get('https://api.spoonacular.com/recipes/random?number=10&apiKey='+api_key+'')
    json_obj = r.json() 
    recipes = json_obj['recipes']['title']
    for x in json_obj:
        print (x)
    return render_template('index.html', random = recipes)

# @app.route('/get_home')
# def get_home():
#     return render_template('index.html')
    # return render_template('index.html', tasks=mongo.db.tasks.find())

@app.route('/get_allRecipes')
def get_allRecipes():
    return render_template('all-recipes.html')
    # return render_template('all-recipes.html', tasks=mongo.db.tasks.find()) 

@app.route('/get_signIn')
def get_signIn():
    return render_template('sign-in.html')
    # return render_template('sign-in.html', tasks=mongo.db.tasks.find())

@app.route('/get_register')
def get_register():
    return render_template('register.html')
    # return render_template('register.html', tasks=mongo.db.tasks.find())    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)