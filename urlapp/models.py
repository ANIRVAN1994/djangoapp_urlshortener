from django.db import models

# Create your models here.
class short_url(models.Model):
    originalurl = models.CharField(max_length=500)
    shorturl = models.CharField(max_length=500)
    websitename = models.CharField(max_length=500)
    urlcount = models.IntegerField()