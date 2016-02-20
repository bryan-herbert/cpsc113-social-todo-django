from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RegistrationManager(models.Manager):
    create_user(
