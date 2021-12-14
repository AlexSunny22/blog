from django.db import models

# Create your models here.
class Blogpost(models.Model):
    post = models.CharField(max_length=1000)
    date = models.DateField()
