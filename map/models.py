from django.db import models


class Locations(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'map_Locations'
