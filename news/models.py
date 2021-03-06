from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=50)
    url_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    url_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
