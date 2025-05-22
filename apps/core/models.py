import uuid

from django.db import models


class APIUUID(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class Base(APIUUID):
    name = models.CharField('Name', max_length=255, db_index=True)
    description = models.TextField('Description', blank=True, null=True, max_length=500)
    stats = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True

class ComplementEmail(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

class UsersBase(APIUUID):
    name = models.CharField('Name', max_length=255, db_index=True)
    email = models.EmailField(unique=True)
    