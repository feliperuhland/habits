from django.core import validators
from django.db import models


class Symptoms(models.Model):
    name = models.CharField(max_length=30)


class Behavior(models.Model):
    name = models.CharField(max_length=90)


class CheckIn(models.Model):
    feeling = models.SmallIntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(9)])
    datetime = models.DateTimeField()
    description = models.TextField(null=True, blank=True)


class CheckInSymptoms(models.Model):
    symptoms = models.ForeignKey(Symptoms, on_delete=models.RESTRICT)
    exaggerated = models.BooleanField()
    check_in = models.ForeignKey(CheckIn, on_delete=models.RESTRICT)


class CheckInBehavior(models.Model):
    behavior = models.ForeignKey(Behavior, on_delete=models.RESTRICT)
    exaggerated = models.BooleanField()
    check_in = models.ForeignKey(CheckIn, on_delete=models.RESTRICT)
