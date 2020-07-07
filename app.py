import os
import requests
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired


if os.path.exists('env.py'):
    import env

""" ENVIROMENT VARIABLES """
app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.environ.get('SECRET_KEY')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

api_key = os.environ['api_key']

# single decoretor '/'set the default function to  call '/index'
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    if 'username' in session:
        return 'You are logged in as'+ session['username']

        r = requests.get(
            'https://api.spoonacular.com/recipes/random?number=10&apiKey='+api_key+'')
        json_obj = r.json()
        recipes = json_obj['recipes']
        return render_template('index.html', recipes=recipes)

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def signIn():
    return render_template('sign-in.html')
# return render_template('sign-in.html', tasks=mongo.db.tasks.find())

@app.route('/get_cuisines', methods=['GET'])
def get_cuisines():
    r = requests.get(
        'https://api.spoonacular.com/recipes/random?number=100&apiKey='+api_key+'')
    obj = r.json()
    recipes = obj['recipes']
    cuisines = obj['cuisines']
    return render_template('all-recipes.html', cuisines=cuisines)


@app.route('/get_allRecipes', methods=['GET'])
def get_allRecipes():
    r = requests.get(
        'https://api.spoonacular.com/recipes/random?number=100&apiKey='+api_key+'')
    obj = r.json()
    types = obj['recipes']
    return render_template('all-recipes.html', types=types)

# VIEW RECIPES DETAILS BY recipe_id
@app.route('/recipe_details/<recipe_id>', methods=['GET'])
def recipe_details(recipe_id):
    r = requests.get(
        'https://api.spoonacular.com/recipes/'+recipe_id+'/information?apiKey='+api_key+'')
    obj = r.json()
    details = obj
    return render_template('recipe-details.html', details=details)


@app.route('/add_recipes', methods=['GET'])
def add_recipes():
    return render_template('add-recipes.html')


@app.route('/my_recipes', methods=['GET'])
def my_recipes():
    return render_template('my-recipes.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = mongo.db.users.find_one({'username': request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username': request.form['username'], 'password' : hashpass })
            session['username'] = request.form['username']
            return redirect(url_for('signIn'))

        return 'That username already exists!'
    return render_template('register.html')

# @app.route('/get_diet', methods=['GET'])
# def get_diet():
#     return render_template('all-recipes.html')
#     # return render_template('register.html', tasks=mongo.db.tasks.find()


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 27017)),
            debug=True)
