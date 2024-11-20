# ---------------------- START ------------------------------

# how to start project?
# go into your directory, open cmd in there and type:
# django-admin startproject (name)

# how to start local serwer?
# go into directory with manage.py
# open cmd in there and type:
# python manage.py runserver (port if needed)

# start new app:
# python manage.py startapp (name)




#----------------------- PATHS ----------------------------
# create endpoints in urls.py (those predefined)
# each endpoint is endpoint to our aplication
# we can ahe multiple aplications in one project
# 
# dont forget to create urls.py in our aplication folder
# 




#--------------------- DATA BASE ---------------------------

# database introduction in django
# add aplication in settings.py (INSTALLED_APPS)
# 'name.apps.NameConfig'

# in models.py create classes that will be used to modify our data

# after that make sure to put this command in cmd:
# python manage.py makemigrations name_of_our_aplication
# THINK OF IT LIKE OF COMMITING IN GITHUB (APPLAYING CHANGES TO OUR PROJECT)
# now use command:
# python manage.py migrate


#------------------ ADMIN PANEL -----------------------------
# how to create superuser
# python manage.py createsuperuser

# how to add our tables into admin panel?
# go to admin.py and type:
# from .models import name1,name2
# admin.site.register(name1)






















# ------------------------ SHELL ------------------------
# python manage.py shell


# in shell you can modify things in database

# make sure to import those items (that you want to modify)
# from app_name.models import item_name, item_name2, item_name3...

# From here you can make variable that stores the data for ex. :
# t = ToDoList(name="Tim\'s List")

# To save it just type 
# variable_name.save()
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

