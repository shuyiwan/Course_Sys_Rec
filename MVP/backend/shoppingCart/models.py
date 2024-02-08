from django.db import models

# These are the configurations of our database tables. Each class below corresponds
# to one table.

# We just do the configuration here, all the data are stored in MySQL server.

# All the tables are in the database with the name "saved_courses_db". You should have
# created this database using MySQL shell commands.

# Go to setting.py to see the connection setting between Django and MySQL server.

# Think each field as the columns of the table. We need to add all the columns here

# Each time you change the models, you need to do migrations:
#   1. python manage.py makemigrations # add the migrations files in migrations
#                                        folder. This file will contain the instructions
#                                        do update database schema 
#   2. python manage.py migrate        # apply the changes

# Each model will automatically have a field id for primary key. It uniquely identifies a 
# row. 

class User(models.Model):
    # username = models.CharField(max_length=30, unique = True) 
    # The username should be unique
    email = models.EmailField(blank = True, null = True, unique = True)

    def __str__(self):
        return self.username

class SavedCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_courses')
    # Forgign key is used to link the class to a user in User table.
    
    # on_delete: when a user is deleted from table, all his saved courses will be
    # automatically deleted as well
    # related_name: help us to find all the courses for a users
    courseID = models.CharField(max_length=30)
    title = models.CharField(max_length = 30, blank = True, null = True)
    instructor = models.CharField(max_length=30, blank = True, null = True)
    description = models.TextField(blank = True, null = True)

    # make sure each user cannot have multiples rows of the same class
    class Meta:
        unique_together = ('user', 'courseID')

    def __str__(self):
        return self.courseID