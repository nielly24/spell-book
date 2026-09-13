from django.db import models
from categories.models import Categories
from accounts.models import Accounts

class Spells(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    incantation = models.TextField(null=True, blank=True)
    difficulty = models.IntegerField()
    mana_cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    category = models.ForeignKey(
        Categories,
        on_delete=models.PROTECT
    )
    created_by = models.ForeignKey(
        Accounts,
        on_delete=models.PROTECT
    )
