from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # name field cannot be empty or int
        if len(postData['name']) < 1:
            errors['name'] = '*Name field is required!'
        elif type(postData['name']) is int:
            errors['name'] = '*Name should not contain number'
        # alias field cannot be empty or int
        if len(postData['alias']) < 1:
            errors['alias'] = '*Alias field is required!'
        elif type(postData['alias']) is int:
            errors['alias'] = '*Alias should not contain number'
        # email have to be a valid and not null
        if len(postData['email']) < 1:
            errors['email'] = '*Email field is required!'
        elif self.filter(email= postData['email']):
            errors['email'] = 'Email address already exists'
        elif  not EMAIL_REGEX.match(postData['email']):
            errors['email'] = '*Invalid email address!'
        # password must have 8 or more characters
        if len(postData['password']) < 1:
            errors['password'] = '*Password field is required!'
        elif len(postData['password']) < 8:
            errors['password'] = '*Password should be at least 8 characters'
        # confirm password must match with password and cannot be empty
        if len(postData['c_password']) < 1:
            errors['c_password'] = 'Confirm password field is required!'
        elif postData['c_password'] != postData['password']:
            errors['c_password'] = 'Password did not match!s'
        return errors

    def login_validator(self, postData):
        errors = {}
        try:
            user = User.objects.get(email = postData['login_email'])
            if len(postData['login_email']) < 1:
                errors['login_email'] = 'Email field is required!'
            if not bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
                errors['password'] = 'Password or email did not match!'
        except User.DoesNotExist:
            errors['invalid'] = 'Your email address or password is wrong'
        return errors


class BookManager(models.Manager):
    def new_book_validator(self, postData):
        errors = {}
        if len(postData['title'])  < 1:
            errors['title'] = '*Book title cannot be empty!'
        return errors

class ReviewManager(models.Manager):
    pass

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    user_book = models.ForeignKey(User, related_name = 'book_users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    user_review = models.ForeignKey(User, related_name = 'review_users')
    book_review = models.ForeignKey(Book, related_name = 'review_books')
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
