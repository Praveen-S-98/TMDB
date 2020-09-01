from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    certificate = models.CharField(max_length=5)
    runtime = models.IntegerField()
    category = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField()
    description = models.CharField(max_length=1000)
    trailer = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='image/', blank=True)
