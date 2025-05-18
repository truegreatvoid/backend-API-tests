import re

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator

from localflavor.br.validators import BRCNPJValidator, BRCPFValidator 

from apps.core.models import Base


def validate_br_document(value):
    digits = re.sub(r'\D', '', value)
    if len(digits) == 11:
        BRCPFValidator()(value)
    elif len(digits) == 14:
        BRCNPJValidator()(value)
    else:
        raise ValidationError(
            'Invalid data. Enter valid CPF or CNPJ.'
        )

class Office(Base):
    name = models.CharField('Name', max_length=255, db_index=True, unique=True)
    cnpj = models.CharField('CPF/CNPJ', max_length=18, unique=True, validators=[validate_br_document])
    location = models.CharField('Localização', max_length=255)
    phone = models.CharField('Telephone', max_length=20, blank=True, null=True,
        validators=[RegexValidator(
                regex=r'^\+?[\d\-\(\) ]{8,20}$',
                message='Invalid phone number.'
            )
        ]
    )
    rooms = models.PositiveIntegerField('Number of Rooms', default=1, validators=[MinValueValidator(1)])

    class Meta:
            verbose_name = 'Office'
            verbose_name_plural = 'Offices'

            

    def __str__(self):
        return f'{self.name} – {self.cnpj}'

   
