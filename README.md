# Simple store to learn Django

## Step 1: Setup and run

1. Clone this project (https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
2. Install requirements: ``pip install -r requirements.txt``
3. Run migrations: ``python manage.py migrate``
4. Start project: ``python manage.py runserver``

## Step 2: Sprint 1 of tasks

1. Add a ``price`` field to ``Product`` (https://www.dev2qa.com/how-to-add-new-model-field-to-exist-django-model/)
2. Add ``price`` field to Add product form
3. Show price on the product details page (http://127.0.0.1:8000/product/view/1)
4. Add a new page for adding a new Category
5. Add a new page for showing the list of categories (Categories page)
6. Show category name of product on the product details page
7. When user will click on category from Categories page show a new page with name of selected category (Category page)
8. On the new category page show list of products from this category