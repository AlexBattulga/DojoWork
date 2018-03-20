from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# >>> a = User(first_name = "Alex", last_name = "Battulga", age = "28")
# >>> a.first_name
# 'Alex'
# >>> a.last_name
# 'Battulga'
# >>> a.age
# '28'
# >>> a.save()
# >>> a.age
# '28'
# >>>
# =========> pulling first and last data from record <==========
# >>> User.objects.first()
# <User: User object>
# >>> User.objects.last()
# <User: User object>
# >>>
# =========> Order by first name <==========
# >>> User.objects.order_by("first_name")
# <QuerySet [<User: User object>, <User: User object>]>
# >>>
# =========> deleting and calling by id <==========
#>>> User.objects.all()
# <QuerySet [<User: User object>, <User: User object>, <User: User object>]>
# >>> User.objects.create(first_name = 'Dan', last_name = 'Batt', age = '58')
# <User: User object>
# >>> User.objects.create(first_name = 'Daniel', last_name = 'Bat', age = '68')
# <User: User object>
# >>> User.objects.get(id=3)
# <User: User object>
# >>> a.first_name
# 'Alex'
# >>> a = User.objects.get(id=1)
# >>> a.delete()
# (1, {u'userLogin.User': 1})
# >>>
