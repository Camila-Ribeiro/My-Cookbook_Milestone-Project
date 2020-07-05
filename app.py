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

# single decoretor '/'set the default function to  call '/index'


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    r = requests.get(
        'https://api.spoonacular.com/recipes/random?number=10&apiKey='+api_key+'')
    json_obj = r.json()
    recipes = json_obj['recipes']
    return render_template('index.html', recipes=recipes)


@app.route('/get_cuisines', methods=['GET'])
def get_cuisines():
    res = requests.get(
        'https://api.spoonacular.com/recipes/random?number=100&apiKey='+api_key+'')
    obj = res.json()
    recipes = obj['recipes']
    cuisines = obj['cuisines']
    return render_template('all-recipes.html', cuisines=cuisines)


@app.route('/get_allRecipes', methods=['GET'])
def get_allRecipes():
    res = requests.get(
        'https://api.spoonacular.com/recipes/random?number=100&apiKey='+api_key+'')
    obj = res.json()
    types = obj['recipes']
    return render_template('all-recipes.html', types=types)

# VIEW RECIPES DETAILS BY recipe_id


@app.route('/recipe_details/<recipe_id>', methods=['GET'])
def recipe_details(recipe_id):
    request = requests.get(
        'https://api.spoonacular.com/recipes/'+recipe_id+'/information?apiKey='+api_key+'')
    obj = request.json()
    details = obj
    return render_template('recipe-details.html', details=details)


@app.route('/add_recipes', methods=['GET'])
def add_recipes():
    return render_template('add-recipes.html')


@app.route('/my_recipes', methods=['GET'])
def my_recipes():
    return render_template('my-recipes.html')

@app.route('/get_signIn')
def get_signIn():
    return render_template('sign-in.html')

#     # return render_template('sign-in.html', tasks=mongo.db.tasks.find())


@app.route('/get_register')
def get_register():
    return render_template('register.html')
    # return render_template('register.html', tasks=mongo.db.tasks.find())

# @app.route('/get_diet', methods=['GET'])
# def get_diet():
#     return render_template('all-recipes.html')
#     # return render_template('register.html', tasks=mongo.db.tasks.find()


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)
