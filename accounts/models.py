from django.contrib.auth.models import AbstractUser
from django.db import models
from roles.models import Roles

class Accounts(AbstractUser):
    display_name = models.CharField(max_length = 200, null = True, blank = True)
    role = models.ForeignKey(
        Roles,
        on_delete = models.PROTECT
    )
