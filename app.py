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
app.jinja_env.add_extension('jinja2.ext.do')

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
        return render_template('index.html', 
        recipes=recipes, 
        current_user=current_user)
    else:
        return render_template('index.html', 
        recipes=recipes
        )

# achieved code using https://www.youtube.com/watch?v=vVx1737auSE&t=621s
# LOGIN 
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


# LOGOUT 
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
            users.insert({'username': request.form['username'], 
                            'password' : hashpass,
                            'avatar': request.form['avatar']  })
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
    user_added_recipes = get_user_recipes()
    
    r = requests.get(
        'https://api.spoonacular.com/recipes/random?number=8&apiKey='+api_key+'')
    obj = r.json()
    random_recipes = obj['recipes']
    return render_template('all-recipes.html', 
        random_recipes=random_recipes, 
        option_allergens=option_allergens,
        option_cuisines=option_cuisines,
        option_diets=option_diets,
        option_meals=option_meals,
        user_added_recipes=user_added_recipes
        )


# GET RECIPES DETAILS from API
@app.route('/recipe_details/<recipe_id>', methods=['GET'])
def recipe_details(recipe_id):
    r = requests.get('https://api.spoonacular.com/recipes/'+recipe_id+'/information?apiKey='+api_key+'')
    # APIused = r.headers.set('X-API-Quota-Used', "default-src 'self'")
    obj = r.json()
    details = obj

    # dup = []
    # for x in details.get('analyzedInstructions'):
    #     for y in x.get('steps'):
    #         for z in y.get('equipment'):
    #             if z['id'] not in dup:
    #                 dup.append(z['id'])
    #                 print(dup)
    return render_template('recipe-details.html', details=details)


# GET USER RECIPES DETAILS from MONGODB
@app.route('/user_recipe_details/<recipe_id>', methods=['GET'])
def user_recipe_details(recipe_id):
    getId = recipe_id
    user_recipe = mongo.db.add_recipes.find_one({'_id':ObjectId(getId)})

    return render_template('user-recipe-details.html', user_recipe=user_recipe)
 

# ADD RECIPES TO MONGODB
@app.route('/add_recipes', methods=['GET', 'POST'])
def add_recipes():
    if 'username' in session:
        current_user = mongo.db.user.find_one({'username': session['username']})
        
        # lists
        option_cuisines = get_cuisines()
        option_allergens = get_allergens()
        option_diets = get_diets()
        option_meals = get_meals()
        
        # add recipes form
        if request.method == 'POST':
            upload_recipe_image = request.files['recipe_image']
            mongo.save_file(upload_recipe_image.filename, upload_recipe_image)
        
            add_recipes = mongo.db.add_recipes
            add_recipes.insert_one({'user_recipe': request.form['user_recipe'],
                'recipe_image': upload_recipe_image.filename,
                'cuisines_list': request.form['cuisines_list'],
                'allergen_list': request.form.getlist('allergen_list'),
                'meal_type_list': request.form.getlist('meal_type_list'),
                'diet_type_list': request.form.getlist('diet_type_list'),
                'recipe_name': request.form['recipe_name'],
                'prep_time': request.form['prep_time'],
                'serves': request.form['serves'],
                'add_ingredients': request.form.getlist('add_ingredients'),
                'add_instructions': request.form.getlist('add_instructions')
                })

            # add_recipes.insert_one(request.form.to_dict())
            return redirect(url_for('add_recipes'))
        return render_template('add-recipes.html', 
            option_diets=option_diets, 
            option_meals=option_meals,
            option_cuisines=option_cuisines, 
            option_allergens=option_allergens)
    else:
        return redirect(url_for('index'))  

   # session['username'] = request.form['username']

# UPDATE RECIPES
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    the_recipe_id = mongo.db.add_recipes
    the_recipe_id.update({"_id": ObjectId(recipe_id)},
    {
    'user_recipe': request.form['user_recipe'],
    'recipe_image': request.form['recipe_image'],
    'cuisines_list': request.form['cuisines_list'],
    'allergen_list': request.form.getlist('allergen_list'),
    'meal_type_list': request.form.getlist('meal_type_list'),
    'diet_type_list': request.form.getlist('diet_type_list'),
    'recipe_name': request.form['recipe_name'],
    'prep_time': request.form['prep_time'],
    'serves': request.form['serves'],
    'add_ingredients': request.form.getlist('add_ingredients'),
    'add_instructions': request.form.getlist('add_instructions')
    })
    return redirect(url_for('my_recipes'))

# MY RECIPES
@app.route('/my_recipes', methods=['GET'])
def my_recipes():
    if 'username' in session:
        #GET CURRENT USER from session
        current_user = session['username'].title()

        #GET CURRENT USER in add_recipes db
        user_added_recipes = mongo.db.add_recipes.find( { "user_recipe": current_user })

        #GET USER DATABASE from user db
        user = mongo.db.users.find_one({"username" : session['username']})

        #COUNTER user recipes
        counting = mongo.db.add_recipes.count_documents({ 'user_recipe': current_user })
   
        return render_template('my-recipes.html', 
            current_user=current_user, 
            user=user,
            counting=counting,
            user_added_recipes=user_added_recipes,
            )
    else:
        return redirect(url_for('index')) 


# EDIT RECIPE
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe_id = mongo.db.add_recipes.find_one({"_id": ObjectId(recipe_id)})

    all_recipe_details = get_user_recipes()
    
    # lists
    option_cuisines = get_cuisines()
    option_allergens = get_allergens()
    option_meals = get_meals()
    option_diets = get_diets()

    #GET SELECTED's OPTIONS
    selected_allergens = the_recipe_id.get('allergen_list')
    selected_meals= the_recipe_id.get('meal_type_list')
    selected_diets = the_recipe_id.get('diet_type_list')

    #GET NOT SELECTED OPTIONS     
    not_selected_allergens = helper_loop(option_allergens, selected_allergens, 'allergen_type')
    not_selected_meals = helper_loop(option_meals, selected_meals, 'meal_type')
    not_selected_diets = helper_loop(option_diets, selected_diets, 'diet_type')     
            
    return render_template('edit-recipe.html',
        recipe_id=the_recipe_id,  
        selected_allergens=selected_allergens,
        not_selected_allergens=not_selected_allergens,
        selected_meals=selected_meals, 
        not_selected_meals=not_selected_meals,
        selected_diets=selected_diets,
        not_selected_diets=not_selected_diets,
        option_cuisines=option_cuisines)

# DELETE RECIPES
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.add_recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_recipes'))

#GET IMAGE FILE
@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

# FUNCTION GET USER ADDED RECIPES
def get_user_recipes():
    user_added_recipes = mongo.db.add_recipes.find()
    return user_added_recipes

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

#GENERIC FUNC LOOP
def helper_loop(options, selected, type):
    arr = []
    for x in options:
        if x[type] not in selected:
            arr.append(x[type])
    return arr

# ERROR PAGE
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error-page.html"), 500

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)
