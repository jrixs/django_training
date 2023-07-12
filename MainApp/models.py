from django.db import models

# Create your models here.
class Colors(models.Model):
   name  = models.CharField(max_length=32)

   def __repr__(self):
      return f'Colors({self.name})'

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   description = models.CharField(max_length=1000)
   colors = models.ManyToManyField(to=Colors)

   def __repr__(self):
      return f'Item({self.name, self.brand, self.count, self.description})'
