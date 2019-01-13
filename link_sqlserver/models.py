from django.db import models


# Create your models here.
class Children(models.Model):
    name = models.CharField(max_length=50)
    age_year = models.IntegerField()
    age_day = models.IntegerField()
    birthday = models.DateField()


class BodyCondition(models.Model):
    children = models.ForeignKey(to=Children,on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    date = models.DateField(default='2019-01-12')
