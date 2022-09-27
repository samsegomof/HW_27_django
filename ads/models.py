from django.db import models


class Category(models.Model):
    """
    Модель категории
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ADS(models.Model):
    """
    Модель ADS
    """
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(blank=True, max_length=2000)
    address = models.CharField(max_length=500)
    is_published = models.BooleanField()

    def __str__(self):
        return self.name
