# Blog Project#


## 1. Installation ##
Install the packages **django,mysqlclient** on virtual environment:

    i.  pip install django    
    ii. pip install mysqlclient
    
### Issue on installing mysqlclient:
Install python3-dev, build-essential,GCC builder to convert library into binaries:

    sudo apt-get install python3 python-dev python3-dev
    build-essential libssl-dev libffi-dev
    libxml2-dev libxslt1-dev zlib1g-dev
    python-pip

    



## 2 Setup ##
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

### 2.1 Setting Up Database ###
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

### 2.2 Setting Up Template:
In **settings**.**py** provide the path of the templates file as:
```python
    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR,'templates')], # setting the templates directory
            ...
            ...
        },
    ]
```

### 2.3 Setting Up Static files:
Documentation: [Static Files Configuration](https://docs.djangoproject.com/en/2.2/howto/static-files/)

Basically for static files(media,template assets,e.t.c) settings we need to define
it's *URL*, *ROOT PATH*,*STATICFILES_DIR*.

Suppose our Project directory to be structured as below:

```
blogproject
    blogproject # created by default
        settings.py 
    blog #appname
        templates # app_wise templates
    staticfiles #local version of static files
    templates # common templates
static_cdn_test 
    media
    static
    
```
Then the settings file can be configured as below: 

```python
STATIC_URL = '/static/' #URL to use when referring to static files located in STATIC_ROOT.

LOCAL_STATIC_CDN_PATH = os.path.join(os.path.dirname(BASE_DIR),'static_cdn_test')
# BASE_DIR = /home/user/Desktop/Django-Tutorial/blogproject
# os.path.dirname(BASE_DIR) = #/home/user/Desktop/Django-Tutorial

STATIC_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH,'static')

STATICFILES_DIR = [  # basically performs lookup on the list of following directories
    os.path.join(BASE_DIR,'staticfiles'),  # local version of static files
    #path1,
    #path2
]

# media, uploaded files storage location 
MEDIA_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH,'media')
MEDIA_URL = '/media/'
```

Finally to use those paths, modify **urls**.**py** as.:
```python
if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
   


  









