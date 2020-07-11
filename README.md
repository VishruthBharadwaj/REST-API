# REST-API
Simple project to store data in JASON Format about user login time ,place 
Here Am using Django Rest Framework

The biggest reason to use Django REST Framework is because it makes serialization so easy!

Steps in Creating REST API:
1.Set up Django
2.Create a model in the database that the 
3.Django ORM will manage
4.Set up the Django REST Framework
5.Serialize the model from step 2
6.Create the URI endpoints to view the serialized data


1.First we need to activate Virtual Environment
1.1Create Django Project(mysite)

1.2 Makesure to check is it working or not by running the server.

1.3Create APIApp inside that--We could build our application with the folder structure the way it is right now. However, best practice is to separate your Django project into separate apps when you build something new.

1.4Register the myapi app with the mysite project
We need to tell Django to recognize this new app that we just created. The steps we do later won’t work if Django doesn’t know about myapi.

1.5 Migrate the database:Whenever we create or make changes to a model, we need to tell Django to migrate those changes to the database. The Django ORM then writes all the SQL CREATE TABLE commands for us.

1.6Created SuperUser


2.Create a model in the database that Django ORM will manage

2.1 myapi/models.py
Let’s make a database of member! Each member has a ID no,Name,Tz,Date.

2.2Make migrations
Whenever we define or change a model, we need to tell Django to migrate those changes.

2.3Register Member with the admin site

2.4Create some new members
While we’re on the admin site, might as well create a few members to play around with in our application.
Click “Add.” Then, make your members!

3. Set up Django REST Framework
 Time to start thinking about our members API. We need to serialize the data from our database via endpoints.


4.Serialize the member model
In this file, we need to:
Import the member model
Import the REST Framework serializer
Create a new class that links the member with its serializer

5.Display the data
Now, all that’s left to do is wire up the URLs and views to display the data!

To do so, we need to:
Query the database for all members
Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered

Test it out!
Start up the Django server again:








