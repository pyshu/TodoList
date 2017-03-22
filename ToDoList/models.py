from django.db import models

# Create your models here.
class Informations(models.Model):
    # id = models.IntegerField(max_length=10,primary_key=True)
    id = models.AutoField(max_length=10,primary_key=True)
    text = models.CharField(max_length=60)
    # datetime = models.DateTimeField(auto_now=False)
    flag = models.BooleanField(max_length=1,choices=((0,'是'),(1,'否')),default=0)