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
@app.route('/index', methods=['GET','POST'])
def index():
    r = requests.get(
        'https://api.spoonacular.com/recipes/random?number=10&apiKey='+api_key+'')
    json_obj = r.json()
    recipes = json_obj['recipes']

    if 'username' in session:
        current_user = mongo.db.user.find_one({'username': session[
            'username'].title()})
        return render_template('index.html', recipes=recipes, current_user=current_user)
    else:
        return render_template('index.html', recipes=recipes)

# LOGIN https://www.youtube.com/watch?v=vVx1737auSE&t=621s
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        allUser = mongo.db.users
        login_user = allUser.find_one({'username' : request.form['username']})
        
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        return 'Invalid username'

    return render_template('login.html')

# SIGN OUT USER
@app.route('/logout',methods=['GET', 'POST'])
def logout():
    if request.method == 'GET':
        session.pop('username', None)
    return redirect(url_for('index'))   

# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username': request.form['username'], 'password' : hashpass })
            session['username'] = request.form['username']
            return redirect(url_for('login'))

        return 'That username already exists!'
    return render_template('register.html')

# GET ALL RECIPES from API
@app.route('/all_recipes', methods=['GET'])
def all_recipes():
    #POPULATE SELECT BOX from mongodb
    option_allergens = get_allergens()
    option_cuisines = get_cuisines()
    option_diets = get_diets()
    option_meals = get_meals()

    r = requests.get(
        'https://api.spoonacular.com/recipes/random?number=8&apiKey='+api_key+'')
    obj = r.json()
    random_recipes = obj['recipes']
    return render_template('all-recipes.html', 
        random_recipes=random_recipes, 
        option_allergens=option_allergens,
        option_cuisines=option_cuisines,
        option_diets=option_diets,
        option_meals=option_meals
        )

# GET RECIPES DETAILS from API
@app.route('/recipe_details/<recipe_id>', methods=['GET'])
def recipe_details(recipe_id):
    r = requests.get(
        'https://api.spoonacular.com/recipes/'+recipe_id+'/information?apiKey='+api_key+'')
    obj = r.json()
    details = obj
    return render_template('recipe-details.html', details=details)

# ADD RECIPES
@app.route('/add_recipes', methods=['GET'])
def add_recipes():
    if 'username' in session:
        current_user = mongo.db.user.find_one({'username': session['username']})
        
        # lists
        option_cuisines = get_cuisines()
        option_allergens = get_allergens()
        option_diets = get_diets()
        option_meals = get_meals()
        
        # if request.method == 'POST':
            #  addCuisine = mongo.db.cuisines select database
            # cuisinesSelect = request.form['cuisines1']
            # users.insert({'username': request.form['username'], 'password' : hashpass })
        return render_template('add-recipes.html', 
            option_diets=option_diets, 
            option_meals=option_meals,
            option_cuisines=option_cuisines, 
            option_allergens=option_allergens)
    else:
        return redirect(url_for('index'))  
    
# MY RECIPES
@app.route('/my_recipes', methods=['GET'])
def my_recipes():
    if 'username' in session:
        current_user = mongo.db.user.find_one({'username': session['username']})
        return render_template('my-recipes.html')
    else:
        return redirect(url_for('index'))  


# FUNCTION TO GET LISTS
def get_cuisines():
    option_cuisines = mongo.db.cuisines.find().sort("cuisine_type", 1)
    return option_cuisines

def get_allergens():
    option_allergens = mongo.db.allergens.find().sort("allergen_type", 1)
    return option_allergens

def get_diets():
    option_diets = mongo.db.diets.find().sort("diet_type", 1)
    return option_diets

def get_meals():
    option_meals = mongo.db.meals.find().sort("meal_type", 1)
    return option_meals

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 27017)),
            debug=True)
