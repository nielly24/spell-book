from django.db import models


class Categories(models.Model):
     name = models.CharField(max_length=200, unique=True)
     description = models.TextField(null = True, blank = True)
