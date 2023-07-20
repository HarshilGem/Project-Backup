from django.db import models

# Create your models here.
class YourModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    checkbox_list = models.BooleanField(default=False)