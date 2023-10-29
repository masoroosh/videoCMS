from django.db import models


class People(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    birth_date = models.DateField(null=True)
    #pic
    #video
