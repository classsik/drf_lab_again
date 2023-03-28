from django.db import models
from django.contrib.auth.models import User


class Exscursion(models.Model):
    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    price = models.IntegerField()


class Country(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.title


TIMES_CHOICES = (
    ('1_week', '1 Неделя'),
    ('2_week', '2 Неделя'),
    ('3_week', '3 Неделя'),
)

SERVICE_CHOICES = (
    ('all_inclusive', 'Все включено'),
    ('not_all_inclusive', 'Не все включено'),
)

STARS_CHOICES = (
    ('3_stars', '3 Звезды'),
    ('4_stars', '4 Звезды'),
    ('5_stars', '5 Звезд'),
)


class Tour(models.Model):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    time_of_stay = models.CharField(max_length=100, choices=TIMES_CHOICES)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    people_count = models.IntegerField()
    hotel = models.CharField(max_length=100, choices=STARS_CHOICES)
    excursions = models.ManyToManyField(Exscursion)
    price = models.IntegerField()


class Cart(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


