from django.db import models

# Create your models here.
class Test_member(models.Model):
    Member_Name = models.CharField(max_length=25)
    Age = models.IntegerField()
    Address = models.CharField(max_length=25)