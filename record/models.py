from django.core import validators
from django.db import models


class Symptom(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Behavior(models.Model):
    name = models.CharField(max_length=90, unique=True)

    def __str__(self):
        return self.name


class CheckIn(models.Model):
    feeling = models.SmallIntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(9)])
    datetime = models.DateTimeField(unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.datetime)


class CheckInSymptom(models.Model):
    symptom = models.ForeignKey(Symptom, on_delete=models.RESTRICT)
    exaggerated = models.BooleanField()
    check_in = models.ForeignKey(CheckIn, on_delete=models.RESTRICT)

    def __str__(self):
        hard = "-hard" if self.exaggerated else ""
        return f"{self.symptom}{hard}"


class CheckInBehavior(models.Model):
    behavior = models.ForeignKey(Behavior, on_delete=models.RESTRICT)
    exaggerated = models.BooleanField()
    check_in = models.ForeignKey(CheckIn, on_delete=models.RESTRICT)

    def __str__(self):
        hard = "-hard" if self.exaggerated else ""
        return f"{self.behavior}{hard}"
