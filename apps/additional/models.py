from django.db import models

from apps.core.models import Base


class Resource(Base):
    class Meta:
        verbose_name = 'Resource'
        verbose_name_plural = 'Resources'

    def __str__(self):
        return f"{self.name} - {self.description}"