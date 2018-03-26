from __future__ import unicode_literals
import re
from django.db import models
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):                                        # form validation for registration
        errors = {}
        if len(postData['fname']) < 1:
            errors['fname'] = 'First name field is required!'
        elif len(postData['fname']) < 3:
            errors['fname'] = 'No fewer than 2 characters!'
        elif type(postData['fname']) is int:
            errors['fname'] = 'First name must have letters only!'

        if len(postData['lname']) < 1:
            errors['lname'] = 'Last name field is required!'
        elif len(postData['lname']) < 3:
            errors['lname'] = 'No fewer than 2 characters!'
        elif type(postData['fname']) is int:
            errors['lname'] = 'Last name must have letters only!'

        if type(postData['email']) < 1:                                         # Checking if email is valid using Regular expression
            errors['email'] = 'Email field is required!'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email address invalid!'
        elif User.objects.filter(email=postData['email']).exists():
            errors['email'] = 'Email address already exists!'

        if len(postData['rpassword']) < 1:
            errors['email'] = 'password field is required!'
        elif postData['rpassword'] != postData['confirmpw']:                    # Checking if password match with confirmpw
            errors['rpassword'] = 'Password did not match!'
        return errors

    def login_validator(self, postData):                                        # Login validation, checking if email and password match with data in the database
        errors = {}
        try:
            user = User.objects.get(email=postData['email'])
            if not bcrypt.checkpw(postData['rpassword'].encode(), user.password.encode()): #passwords do not match
                errors['rpassword'] = "Invalid email address or password."
        except User.DoesNotExist:
            if len(postData['email']) < 1:
                errors['email'] = 'Email field cannot be empty!'
            elif not EMAIL_REGEX.match(postData['email']):
                errors['email'] = 'Email address invalid!'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    confirmpw = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
