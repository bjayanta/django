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

- Making queries
    - Retrieving and filtering objects 
    - Basic queries 
        - create
        - save
        - update
        - get
        - filter
        - delete 
    - Querying and filtering related objects
    - Complex lookups with Q (combining or, and operators)
    - Querying and filtering JSONField

- Aggregation 
    - Introduction & Basics
    - Join related models and aggregate
    - Combining aggregations, annotations and filtering

- Advanced search with postgres extensions

- Performing raw SQL queries 

- Database transactions
    - Atomic transactions (making view functions atomic)
    - on_commit, savepoints (nested atomic transactions)

- Multiple databases 
    - Defining multiple databases, manually selecting db
    - Database routers, automatic db routing

- Database access optimization 
    - Indexes, tablespaces
    - Queryset optimization
    - Bulk methods

- URL dispatcher 
    - Basics, converters, extra parameters, include
    - Custom converters and regular expressions in re_path
    - Path names, namespaces, name resolution with reverse()

- Writing views 
    - Basics, errors, custom error views
    - Decorators

- Upload 
    - Single file
    - Multiple files 
    - Save file(s) to model

- Shortcuts

- Middleware 
    - Writing your own middleware
    - Hooks, streaming http, async decorator

- Sessions 
    - Configuration (enabling, engines, settings, clearing)
    - Using sessions in views and shell

- Forms 
    - Render with template, receive data
    - Bounding, widgets, ways to display in template

- Formsets 
    - Defining, displaying, getting data from formset
    - Validation, errors
    - Order, delete, extra fields and parameters, prefixes

- Modelforms 
    - Create, display form, save model
    - Meta, inheritance, edit objects
    - Model formsets

- Form Assets 
    - Media class (css and js for forms)

- Templates
    - Language, rendering, settings

- Class Based Views 
    - Introduction and overview
    - Built-in generic views (ListView, DetailView)
    - Models (create, update, list, delete, detail)
    - Mixins concept, combining mixins and views

- Migrations 
    - Concept, operations, files, different databases
    - Advanced Migrations
        - Reverse
        - squash
        - custom fields
        - migrate data

- Files 
    - Opening, writing, saving to models, file storage options

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
> pip install -r .\requirements.txt

