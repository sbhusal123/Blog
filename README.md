# Django Tutorials #
Hands on django rest framework.

## 1. Installation ##
Install the packages **django** on virtual environment:

    i.  pip install django    
    ii. pip install mysqlclient
    
### Issue on installing mysqlclient:
Install python3-dev, build-essential,GCC builder to convert library into binaries:

    sudo apt-get install python3 python-dev python3-dev
    build-essential libssl-dev libffi-dev
    libxml2-dev libxslt1-dev zlib1g-dev
    python-pip

    



### 1.1 Setup ###
i. Create a django project `django-admin startproject <project_name>`

ii. Create an app switching to directory where **manage**.**py** is located:
* `python manage.py startapp <appname>`
* Now add the app thus created to the **INSTALLED_APPS** application under **settings**.py:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<app name>', #name of the app you've created
]
```

### 1.2 Setting Up Database ###
First of all create a database named **<database_name>** then in the **settings**.**py** file change default database as :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database_name>',
        'USER': '<user_name>',
        'PASSWORD': '<database_password>',
        'HOST': '<host_address>',
        'PORT': '<host_port>',
        'OPTIONS':{ 
            'read_default_file': 'path/to/cnf/file/for/database/server',
        },
       # OPTIONS fiels is not mandatory. It's necessary when django can't find database 
       # configurations by default
        
       
    }
}
```
* Then create migrations to append changes on databases : ```python manage.py makemigrations <app_name>```. Basically what this does is creates a **.py** file for performing changes to the database you've created. Those  files for performing migrations is located at **app_name/migrations** directory.

* Now migrate the state of database from one state to another: `python manage.py migrate`. Actually what this does is executes .py files we've discussed above.

> Note: Everytime the database changes are made(*creating new tables, altering the tables*),then at first create the migrations and perform migration.







