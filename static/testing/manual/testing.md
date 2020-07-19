## Testing

#### NavBar:
I tested to make sure the following worked as designed and All passed

###### When logged in, the user sees the following pages:
- Index
- All Recipes
- My Recipes
- Add Recipes
- User Nav - Username (redirect the user to My recipes page) & Log Out

All the routs are working accordingly:
1. Click on Index which is 'My CookBook' logo (route to '/index').
2. Click on All Recipes (route to /all_recipes).
3. Click on My Recipes (route to /my_recipes).
   - username has no recipes added (No recipes yet - Add your first recipe(button)).

###### When not logged in, the user sees the following pages:
- Index
- All Recipes
- Login
- Register

All the routs are working accordingly:
1. Click on Index which is 'My CookBook' logo (route to '/index').
2. Click on All Recipes (route to /all_recipes).
3. Click on Login (route to /login).
4. Click on Register (route to /register).


#### Index(route '/index'):
###### Get Inspired section
1. Click on Index which is 'My CookBook' logo (route to '/index').
2. Go to the "Get Inspired" section.
3. Try to click on a recipe's name underneath recipes images to verify if it is opening the "recipe-details.html" page containing detailed information about the same recipe shown on recipe's card on index.html page.
4. Try to click on a forward and backwards arrows to verify if it's displaying another recipes.

###### When logged in, the user sees "Make your own Cookbook" section:
5. Try to click on "Add your Recipes" to verify if it's redirecting to "Add Recipe" page.
6. Try to click on "Edit & Delete Recipes" to verify if it's redirecting to "Edit Recipe" page.
7. Try to click on "Share your Recipes" to verify if it's redirecting to "My Recipes" page.

###### When not logged in, the user sees "How thir website works" section:
8. Try to click on "Register" to verify if it's redirecting to "Register" page.
9. Try to click on "Create your recipes" to verify if it's redirecting to "Add Recipe" page.
10. Try to click on "Share with Friends" to verify if it's redirecting to "My Recipes" page.

#### Log In: WIP
1. Click on "Login"on menu.
2. Try to insert a username. 
3. Try to insert a password. 
4. Try to insert a username and click on "Login".


#### Register: WIP


#### All Recipes(route /'all_recipes')
1. Click on "All recipes" page.
2. Try to click on the "Diet Label" filter to verify if it is displaying recipes related to the filter chosen.
3. Try to click on the "Allergen" filter to verify if it is displaying recipes related to the filter chosen.
4. Try to click on the "Meal Type" filter to verify if it is displaying recipes related to the filter chosen.
5. Try to click on the "Diet Label" filter to verify if it is displaying recipes related to the filter chosen.
6. Try to click on a recipe's name underneath recipes images to verify if it is opening the "recipe-details.html" page containing detailed information about the same recipe.

###### Inspiration Recipes:
1. Try to click on a recipe's name underneath recipes images to verify if it is opening the "recipe-details.html" page containing detailed information about the same recipe.

###### When user is logged in:
###### Recipes by Username:
1. Try to click on a recipe's name underneath recipes images to verify if it is opening the "recipe-details.html" page containing detailed information about the same recipe.


#### Recipes Details (route /'recipe_details'):
1. Check is all fields are complete with information and not empty.


#### My Recipes (route/ 'my_recipes'):
1. Click on "My recipes" page.
2. Try to click on recipes card's title to verify if it is opening the user-recipe-detais.html page
3. Try to click on "Edit" button to verify if it is opening the edit-recipe.html page 
4. Try to click on "Bin icon" to verify if it is deleting the recipe.


#### Add Recipe (route /'add_recipes'):
1. Click on "Add recipes" page.
2. Try to click on the "Cuisines" filter to verify if it is displaying type of cuisines available to choose.
3. Try to click on the "Allergen" filter to verify if it is displaying type of allergens available to choose.
4. On Allergen filter try to select up to 4 options to verify if it is marked as selected.
5. Try to click on the "Meal type" filter to verify if it is displaying type of meals available to choose.
6. On Meal type filter try to select up to 4 options to verify if it is marked as selected.
7. Try to click on the "Diet Label" filter to verify if it is displaying type of diets available to choose.
8. On Diet label filter try to select up to 4 options to verify if it is marked as selected.
9. Try to click on input "Recipe Name" to verify if it is accepting text.
10. Try to click on button "Choose file" to verify if it is opening a window to browse files to upload.
11. Try to click on input "Preparation time" to verify if it is accepting text or if arrows are working.
12. Try to click on input "Serves" to verify if it is accepting text or if arrows are working.
13. Try to click on input "add ingredient" to verify if it is accepting text.
14. Try to click on button "Add more" to verify if it is displaying a new input to add more ingredients.
16. Try to click on button "delete" to verify if it is deleting the input to add ingredient.
17. Try to click on input "add instruction" to verify if it is accepting text.
18. Try to click on button "Add more" to verify if it is displaying a new input to add more instructions.
19. Try to click on button "delete" to verify if it is deleting the input to add instruction.
20. Try to click on button "Add recipe" to verify if the recipe is added successfuly. 


#### Edit Recipe (route /'edit_recipe'):
1. Click on "Edit recipes" page.
2. Try to click on the "Cuisines" filter to verify if it is displaying type of cuisines available to choose.
3. Try to click on the "Allergen" filter to verify if it is displaying type of allergens available to choose.
4. On Allergen filter try to select up to 4 options to verify if it is marked as selected.
5. Try to click on the "Meal type" filter to verify if it is displaying type of meals available to choose.
6. On Meal type filter try to select up to 4 options to verify if it is marked as selected.
7. Try to click on the "Diet Label" filter to verify if it is displaying type of diets available to choose.
8. On Diet label filter try to select up to 4 options to verify if it is marked as selected.
9. Try to click on input "Recipe Name" to verify if it is accepting text.
10. Try to click on button "Choose file" to verify if it is opening a window to browse files to upload.
11. Try to click on input "Preparation time" to verify if it is accepting text or if arrows are working.
12. Try to click on input "Serves" to verify if it is accepting text or if arrows are working.
13. Try to click on input "add ingredient" to verify if it is accepting text.
14. Try to click on button "Add more" to verify if it is displaying a new input to add more ingredients.
16. Try to click on button "delete" to verify if it is deleting the input to add ingredient.
17. Try to click on input "add instruction" to verify if it is accepting text.
18. Try to click on button "Add more" to verify if it is displaying a new input to add more instructions.
19. Try to click on button "delete" to verify if it is deleting the input to add instruction.
20. Try to click on button "Edit recipe" to verify if it redirects to "My recipes" page.


#### User Recipe Details (route /'user_recipe_details'):
1. Try to click on button "Edit recipe" to verify if it redirects to "Edit Recipe" page.
2. Try to click on "Bin icon" to verify if it is deleting the recipe and redirects to "My recipes" page.


#### Error Page
1. Try to click on link "here" to verify if it redirects back to the homepage/index.