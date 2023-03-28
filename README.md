# Guitar Configurator Django
Webapp that allows you to build your own custom guitar

# Database Setup
Install XAMPP (8.2.0) and select the Apache and MySQL Modules.
Start Apache and MySQL.
Create a database with the name "guitardb".

# Installation
When cloning this project you need to create your own virtual environment in which all the dependencies have to be installed. <br>
Create the Virtual Environment in the projects directory:

*Linux / MacOS*
```
python3 -m venv env
```

*Windows*
```
py -m venv env
```

# Install dependencies 
To install the dependencies run this command in the projects directory:

*Linux / MacOS*
```
pathToYourEnvironment/bin/python -m pip install -r requirements.txt
```

*Windows*
```
pathToYourEnvironment\bin\python -m pip install -r requirements.txt
```

# Updating dependencies
If the dependencies will change later, you need to update the requirements.txt by running this command in the projects directory:

*Linux / MacOS*
```
pathToYourEnvironment/bin/python -m pip freeze > requirements.txt
```

*Windows*
```
pathToYourEnvironment\bin\python -m pip freeze > requirements.txt
```

# Activate the virtual environment

*Linux / MacOS*
```
source env/bin/activate
```

*Windows*
```
.\env\Scripts\activate
```

# Migrate the Django model and populate the database with a fixture

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Load the fixture:
```
python manage.py loaddata database.json
```

# Start the Django Application

```
python manage.py runserver 8000
```
Now visit http://127.0.0.1:8000/ 