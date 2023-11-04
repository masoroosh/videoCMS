from django.db import models
from cast.models import Person


class TVShow(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Season(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    tvshow = models.ForeignKey(TVShow, on_delete=models.PROTECT)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.tvshow.title + ' | ' + self.title


class Collection(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class People(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Video = models.ForeignKey('Video', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)


class Video(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    season = models.ForeignKey(Season, on_delete=models.PROTECT)
    order = models.IntegerField(default=1)
    collection = models.ManyToManyField(Collection, through='CollVideo')
    tag = models.CharField(max_length=255)  # should be a generic model
    person = models.ManyToManyField(
        Person, through=People)  # should be a generic model
    album = models.CharField(max_length=255)

    def __str__(self):
        return self.season.tvshow.title+' | ' + self.season.title + ' | '+self.title


class CollVideo(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    video_order = models.IntegerField(default=1)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)


class Duble(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=255)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class Subtitle(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=255)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
