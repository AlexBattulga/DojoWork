from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)

class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(Dojo, related_name = 'ninjas')

#================> Create 3 dojos and delete <================
# >>> from apps.dojo_ninjas.models import *
# >>> Dojo.objects.create(name = 'CodingDojo Silicon Valley', city = 'Mountain View', state = 'CA')
# <Dojo: Dojo object>
# >>> Dojo.objects.create(name = 'CodingDojo Silicon Seattle', city = 'Seattle', state = 'WA')
# <Dojo: Dojo object>
# >>> Dojo.objects.create(name = 'CodingDojo Silicon New York', city = 'New York', state = 'NY')
# <Dojo: Dojo object>
# >>> Dojo.objects.get(id=1).delete()
# (1, {u'dojo_ninjas.Ninja': 0, u'dojo_ninjas.Dojo': 1})
# >>> Dojo.objects.get(id=2).delete()
# (1, {u'dojo_ninjas.Ninja': 0, u'dojo_ninjas.Dojo': 1})
# >>> Dojo.objects.get(id=3).delete()
# (1, {u'dojo_ninjas.Ninja': 0, u'dojo_ninjas.Dojo': 1})
# >>>
#================> Create 3 dojos and 3 ninjas that belongs to specific dojo <================
# >>> Dojo.objects.create(name = 'CodingDojo Silicon Valley', city = 'Mountain View', state = 'CA')
# <Dojo: Dojo object>
# >>> Dojo.objects.create(name = 'CodingDojo Silicon Seattle', city = 'Seattle', state = 'WA')
# <Dojo: Dojo object>
# >>> Dojo.objects.create(name = 'CodingDojo Silicon New York', city = 'New York', state = 'NY')
# <Dojo: Dojo object>

# d = Dojo(name = 'CodingDojo Silicon Valley', city = 'Mountain View', state = 'CA')
# d.save()
# d1 = Dojo(name = 'CodingDojo Silicon Seattle', city = 'Seattle', state = 'WA')
# d1.save()
# d2 = Dojo(name = 'CodingDojo Silicon New York', city = 'New York', state = 'NY')
# d2.save()
# ==================> Created ninjas for first dojo <===================
# n = Ninja(first_name = 'Enkhbaatar', last_name ='Battulga', dojo = d)
# n.save()
# n1 = Ninja(first_name = 'Julian', last_name = 'Yondai', dojo = d)
# n1.save()
# n2 = Ninja(first_name = 'Saruul', last_name = 'Tsog', dojo = d)
# n2.save()
# ==================> Created ninjas for second dojo <===================
# n = Ninja(first_name = 'Enkh', last_name ='Batt', dojo = d1)
# n.save()
# n1 = Ninja(first_name = 'Jul', last_name = 'Yond', dojo = d1)
# n1.save()
# n2 = Ninja(first_name = 'Sar', last_name = 'Tsogoo', dojo = d1)
# n2.save()
# ==================> Created ninjas for last dojo <===================
# n = Ninja(first_name = 'Enkh', last_name ='Battulga', dojo = d2)
# n.save()
# n1 = Ninja(first_name = 'Julia', last_name = 'Yond', dojo = d2)
# n1.save()
# n2 = Ninja(first_name = 'Sara', last_name = 'Tsoglog', dojo = d2)
# n2.save()
