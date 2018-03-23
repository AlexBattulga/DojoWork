from __future__ import unicode_literals

from django.db import models
class NameManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = 'Course name should be more than 5 characters!'
        if len(postData['desc']) < 16:
            errors['decs'] = 'Course description should be more than 15 characters'
        return errors
class Desc(models.Model):
    course_desc = models.TextField()

class Name(models.Model):
    course_name = models.CharField(max_length = 255)
    desc = models.OneToOneField(Desc, on_delete=models.CASCADE, default='d')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = NameManager()

    def __str__(self):
        return 'Course Info: %s %s' % (self.course_name, self.course_desc)
