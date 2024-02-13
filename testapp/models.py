from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=15)
    sid = models.IntegerField()
    smarks=models.FloatField()

    def get_absolute_url(self):
        return '/list'

    