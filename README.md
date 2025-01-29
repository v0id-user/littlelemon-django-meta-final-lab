# Little Lemon Restaurant

This a the final lab from [Meta's Django course](https://www.coursera.org/learn/django-web-framework). Where I'm required to built upon and improve a restaurant website called "Little Lemon".

# Little Lemon Restaurant To-Do List

## Goal
- [ ] Build two pages for the web app:
  - [ ] Create the Menu page
  - [ ] Create the Menu Item page

## Learner Instructions
- [ ] The Little Lemon website will have five pages:
  - [ ] Home
  - [ ] About
  - [ ] Booking
  - [ ] Menu
  - [ ] Menu Item
- [ ] Modify the following files:
  - [ ] settings.py
  - [ ] urls.py (app-level)
  - [ ] models.py
  - [ ] views.py
  - [ ] admin.py
  - [ ] templates/menu.html
  - [ ] templates/menu_item.html
  - [ ] templates/partials/_footer.html

## Steps
### Part 1 – Create the Menu page
- [ ] Step 1: Open models.py and create a class called Menu with attributes:
  - [ ] name (CharField, max_length=200)
  - [ ] price (IntegerField)
  - [ ] Define __str__() method.
- [ ] Step 2: Open admin.py and register the Menu model.
- [ ] Step 3: Run commands to make and perform migrations.
- [ ] Step 4: Check URL configurations in project-level and app-level urls.py.
- [ ] Step 5: Add data to the model using the Django admin panel.
- [ ] Step 6: Create a superuser.
- [ ] Step 7: Add menu items in the Django admin panel.
- [ ] Step 8: Open views.py and create a view function for the menu page.
- [ ] Step 9: Add view logic to fetch menu data.
- [ ] Step 10: Update app-level urls.py with the menu view path.
- [ ] Step 11: Create menu.html and add starter code.
- [ ] Step 12: Add Django Template Language (DTL) for menu items.
- [ ] Step 13: Run the development server and check the homepage.

### Part 2 – Create the Menu item page
- [ ] Step 1: Update Menu model in models.py with description (TextField).
- [ ] Step 2: Update menu items in the Django admin panel.
- [ ] Step 3: Create display_menu_items view in views.py.
- [ ] Step 4: Define view logic for display_menu_items.
- [ ] Step 5: Add path for menu item view in app-level urls.py.
- [ ] Step 6: Update menu.html to link to menu item page.
- [ ] Step 7: Create menu_item.html and add starter code.
- [ ] Step 8: Replace comments in menu_item.html with DTL.
- [ ] Step 9: Run migrations and server, then check menu item page.

### Part 3 – Create the footer template
- [ ] Step 1: Update _footer.html with footer code.
- [ ] Step 2: Replace image source in _footer.html.
- [ ] Step 3: Include footer in base.html.

## Additional Steps
- [ ] Make a reservation on the Little Lemon website.
- [ ] Check reservation data in the database.
