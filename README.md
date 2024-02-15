# LAB - Class 28

## Project: Django CRUD and Forms

### Project Description

This django built web app utilizes multiple Django Models to allow data to persist using Python objects (models). The models define the structure of stored dta, including the field types, max size, default values, etc. The app includes full CRUD functionality that allows Creating, Reading, Updating and Deleting snacks.

### Author: Rhett Chase

### Links and Resources

<!-- - [back-end server url](https://capital-finder-rhett-chase.vercel.app/api) -->
<!-- - [front-end application](http://xyz.com/) (when applicable) -->
- chatGPT
- [Django Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
- [Django Templates](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page)
- [Django Views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)

### Setup

- `pip install -r requirements.txt`

#### `.env` requirements (where applicable)

<!-- i.e.
- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db -->
- N/A

#### How to initialize/run your application (where applicable)

- Clone repo
- Install dependencies (see above)
- See the page in browser by running `python manage.py runserver`
- Open the page via the local server address specified in the terminal

##### Create Superuser

- In separate terminal, create superuser with command `python manage.py createsuperuser`
- Visit the `/admin` path and login with the superuser username and password you created

##### Create, Update, Delete Snacks

- **`Read`**: Visit the home directory (snack list) view the full list of snacks `http://127.0.0.1:8000/`
- **`Create`**: Click on `Create New Snack` button and complete the form, then click `Save`
- **`Update` and `Delete`**: Return to home (snack list), then click on a snack you want to delete or update
- Click update or delete
- Confirm your choice (click save to update or OK to delete, depending on the selection)

#### How to use your library (where applicable)

- N/A

#### Tests

- `python manage.py test`
