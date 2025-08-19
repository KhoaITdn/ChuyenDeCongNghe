from django.db import models

SHIRT_SIZES = [
    ("S", "Small"),
    ("M", "Medium"),
    ("L", "Large"),
]

class Person(models.Model):
    name = models.CharField(max_length=60, default='anonymous')
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default='M')

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType, max_length=10)

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)        