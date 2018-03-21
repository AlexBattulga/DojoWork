from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    notes = models.TextField(1000, default = 'DEFAULT VALUE')
    books = models.ManyToManyField(Book, related_name = 'authors')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# ===============> Creating a 5 books <==================
# >>> from apps.book_authors.models import *
# c = Book(name = 'C sharp')
# c.save()
# j = Book(name = 'Java')
# j.save()
# p = Book(name = 'Python')
# p.save()
# ph = Book(name = 'PHP')
# ph.save()
# r = Book(name = 'Ruby')
# r.save()
# ===============> Creating a 5 authors <==================
# a_m = Author(first_name = 'Mike')
# a_m.save()
# a_s = Author(first_name = 'Speros')
# a_s.save()
# a_j = Author(first_name = 'John')
# a_j.save()
# a_jd = Author(first_name = 'Jadee')
# a_jd.save()
# a_jay = Author(first_name = 'Jay')
# a_jay.save()
# ===============> Using the shell <==================
# r.name = 'C#'
# r.save()
# r.name
# C#

# >>> a_jay.first_name = 'Ketul'
# >>> a_jay.save()
# >>> a_jay.first_name
# 'Ketul'
# >>>
