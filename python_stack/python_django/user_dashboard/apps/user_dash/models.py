from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
#Basic validation for registration
    def basic_validator(self, postData):
        errors = {}
        # email validation
        if len(postData['email']) < 1:
            errors['email'] = 'Email field is required!'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'
        elif User.objects.filter(email=postData['email']).exists():
            errors['email'] = 'Email address is already exists'
        #first and last name validation
        if len(postData['fname']) < 1:
            errors['fname'] = 'First name field is required'
        elif type(postData['fname']) is int:
            errors['fname'] = 'First name field must have characters only!!'
        if len(postData['lname']) < 1:
            errors['lname'] = 'Last name field is required'
        elif type(postData['lname']) is int:
            errors['lname'] = 'Last name field must have characters only!!'
        #Password validation
        if len(postData['password']) < 1:
            errors['password'] = 'Password field cannot be empty'
        elif len(postData['password']) < 9:
            errors['password'] = 'Must be more than 8 characters'

        if len(postData['confirm_pw']) < 1:
            errors['confirm_pw'] = 'Confirm password field cannot be empty'
        elif postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = 'Confirm password did not match'
        return errors
#Login validation
    def login_validator(self, postData):
        errors = {}
        try:
            user = User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = 'Invalid email or password'
        except User.DoesNotExist:
            if len(postData['email']) < 1:
                errors['email'] = 'Email field cannot be empty'
            elif not EMAIL_REGEX.match(postData['email']):
                errors['email'] = 'Invalid email address'
        return errors
# Edit user validation
    def edit_validator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['email'] = 'Email field is required!'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'
            #first and last name
        if len(postData['fname']) < 1:
            errors['fname'] = 'First name field is required'
        elif type(postData['fname']) is int:
            errors['fname'] = 'First name field must have characters only!!'
        if len(postData['lname']) < 1:
            errors['lname'] = 'Last name field is required'
        elif type(postData['lname']) is int:
            errors['lname'] = 'Last name field must have characters only!!'
        return errors
# password update
    def password_update_validator(self, postData):
        errors = {}
        #Password validation
        if len(postData['password']) < 1:
            errors['password'] = 'Password field cannot be empty'
        elif len(postData['password']) < 9:
            errors['password'] = 'Must be more than 8 characters'

        if len(postData['confirm_pw']) < 1:
            errors['confirm_pw'] = 'Confirm password field cannot be empty'
        elif postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = 'Confirm password did not match'
        return errors
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name = 'messages')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Comment(models.Model):
    comment = models.TextField()
    user_message = models.ForeignKey(Message, related_name = 'comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
