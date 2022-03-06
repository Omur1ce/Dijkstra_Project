from django.db import models

class Person(models.Model):
    form = models.CharField(max_length=30, null = True)
