## Testing

#### NavBar:
I tested to make sure the following worked as designed and All passed

When logged in the user sees the following pages
- Index
- All Recipes
- My Recipes
- Add Recipes
- User Nav - Username (redirect the user to My recipes page) & Log Out

Click on Add Recipes icon (route to /<username>/add_recipe)
Click on My Recipes icon (route to /<username>/by_my_recipes)
if there are no recipes by username (Message saying You don't have any recipes !)
When not signed in you see the following icons (Home, All Recipes, Add Recipes, Sign in & Register)
Click on Home icon (route to /base)
Click on All Recipes icon (route to /by_recipes)
Click on sign in icon (route to /sign_in_user)
Click on Register icon (route to /register_user)

#### Index:
###### Inspire Me section
1. Go to the "Inspire Me" section
2. Try to click on a photo from Hotel's card which displays three photos to verify if it is opening the "detail-page.html" page containing information about the same place shown on Hotel's card on index.html page
3. Try to click on a hotel's name title from Hotels card which displays three photos to verify if it is opening the "detail-page.html" page containing information about the same place shown on Hotel's card on index.html page
4. Try to click on a photo from Restaurant's card which displays three photos to verify if it is opening the "detail-page.html" page containing information about the same place shown on Restaurant's card on index.html page
5. Try to click on a restaurant's name title from Restaurant's card which displays three photos to verify if it is opening the "detail-page.html" page containing information about the same place shown on Restaurant's card on index.html
6. Try to click on a photo from Museums's card which displays three photos to verify if it is opening the "detail-page.html" page containing information about the same place shown on Museums's card on index.html page
7. Try to click on a museum's name title from Museum's which displays three photos to verify if it is opening the "detail-page.html" page containing information about the same place shown on Museum's card on index.html page
8. Try to click on "Contact Us" from the Menu navigation to verify if it is opening the contact.html
9. Bugs were detected when sometimes information(data) about hotels, restaurantes or museums appear duplicated or triplicated on Inspire Me section. I tried to fix it but I couldn't. It is a feature left to implement later after I graduate from the course.

#### Log In:

#### Register:

#### All Recipes / all_recipes :
1. Go to the "Search Resuts" page
2. Try to click on the "Curious World" logo to verify if it is opening the index.html page
3. Try to click on "Contact Us" from the Menu navigation to verify if it is opening the contact.html page
4. Try to click on the "Previous/Next" arrows on "pagination" and verify if it is working backwards and forwards displaying current pages without any errors
      1. If current page is page 2 try to click on Previous button to verify if previous button is hidden after page 1 is active
      2. If current page is the last page verify if next button is hidden
      3. If current page is page before last page try to click on next button to verify if next button is hidden after last page is active
5. From current page, try to click the "Previous/Next" arrows on "pagination" and verify if it is working backwards and forwards displaying current active pages
6. If current page is page 1, try to click on any page number to verify if is active
7. From page 1:
      1. Try to click on page 2 to verify if it is displaying 10 new places or the remaining amount of places left if page 2 is the last    page on pagination
      2. Try to click on page 3 to verify if it is displaying 10 new places or the remaining amount of places left if page 3 is the last    page on pagination
      3. Try to click on page 4 to verify if it is displaying 10 new places or the remaining amount of places left if page 4 is the last    page on pagination
      4. Try to click on page 5 to verify if it is displaying the remaining amount of places left on pagination   
8. Check if Heading title changes on Search results page for Hotels in California 
9. Check if Heading title changes on Search results page for Restaurants in California 
10. Check if Heading title changes on Search results page for Museums in California

##### Recipes Details / recipe_details:

#### My Recipes / my_recipes:
1. Page access only from "Inspire me" section on index.html page by clicking on one of the displayed photos os place's titles OR from "read more" button displayed on cards in the search-results.html
2. Try to click on the "Curious World" logo to verify if it is opening the index.html page
3. Try to click on "Contact Us" from the Menu navigation to verify if it is opening the contact.html page 
4. Try to click on the "Previous/Next" arrows on Slideshow and verify if it is working backwards and forwards displaying pictures without any errors
5. Try to click on "website" link to verify if it is opening the website address in a new window 
6. Try to click on "Phone Number" link to verify if it is redirecting to call from user's device

#### Add Recipes / add_recipes:

#### Edit Recipes / edit_recipes:

##### User Recipes Details / user_recipe_details:

#### Error Page