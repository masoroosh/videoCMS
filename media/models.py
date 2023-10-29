from django.db import models


class CmsModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Video(CmsModel):
    title = models.CharField(max_length=255)


class Series(CmsModel):
    title = models.CharField(max_length=255)


class Season(CmsModel):
    title = models.CharField(max_length=255)


class Collection(CmsModel):
    title = models.CharField(max_length=255)


class Film(CmsModel):
    title = models.CharField(max_length=255)
    season = models.ForeignKey(Season, null=True, blank=True)
    collection = models.ForeignKey(Collection, null=True, blank=True)
    tag = models.CharField(max_length=255)  # should be a generic model
    cast = models.CharField(max_length=255)  # should be a generic model
    album = models.CharField(max_length=255)
    # episode


class Duble(CmsModel):
    language = models.CharField(max_length=255)
    film = models.ForeignKey(Film)


class Subtitle(CmsModel):
    language = models.CharField(max_length=255)
    film = models.ForeignKey(Film)
