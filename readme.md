# Django(Full Course) Practice
Welcome to the "Django course" and become an expert.

## Topics 
- Installation & Configurations 
- Models
    - Introduction 
    - Fields and field types
    - Field options (default, verbose, primary key), migration
    - Relations 
        - One to Many
        - Many to Many
        - One to One
    - Difference between blank and null options
    - Recursive relations, related names 
    - Field validation
    - Writing Custom Fields 
    - Meta options 
    - Managers 
    - Methods
    - Inheritance and abstract base classes
    - Multi-table inheritance 
    - Proxy models inheritance
    - Multiple inheritance (from multiple classes/models) 

## Installation

### Step 1:
Install & create virtual environment 
> pip install virtualenv

> pip -m venv \<env-name>

### Step 2:
Activate virtual environment (Windows)
> cd \<env-name>\Scripts\

> activate

### Step 3:
Install Django
> pip install django

### Step 4:
Install [MySQL Client](https://pypi.org/project/mysqlclient/)
> pip install mysqlclient 

### Step 5:
Serve the server.
> python manage.py runserver 

or, 
> python manage.py runserver \<ip-address>:\<port-number>

Do not forgot to update "ALLOWED_HOSTS" from project settings.

### Step 6:
Make migrations & migrate to database 
> python manage.py makemigrations

> python manage.py migrate

### Step 7:
Create superadmin
> python manage.py createsuperuser 

# Step 8:
Generate dependance list
> pip freeze > requirements.txt

Install dependance recursively
> pip install -r requirements.txt

