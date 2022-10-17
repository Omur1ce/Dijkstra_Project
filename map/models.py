from django.db import models

class Person(models.Model):
    form = models.CharField(max_length=30, null = True)

class Result(models.Model):
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

    