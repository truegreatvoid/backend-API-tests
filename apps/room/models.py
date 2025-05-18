from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from apps.core.models import Base

class Room(Base):
    STATUS_CHOICES = [
        ('available','Available'),
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Cancelled'),
    ]

    office = models.ForeignKey("office.Office", on_delete=models.DO_NOTHING, related_name='room')
    location = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='available')
    time_global = models.CharField(max_length=50, blank=True, null=True)
    resources = models.ManyToManyField(
            "additional.Resource",
            related_name='room',
            blank=True
        )

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return f"{self.name}"  
    
    def clean(self):
        if not self.office_id:
            raise ValidationError('This room needs to be linked to an office.')

class Reservation(models.Model):
    room = models.ForeignKey("room.Room", on_delete=models.DO_NOTHING, related_name='reservations')
    customers = models.ForeignKey("customers.Customers", on_delete=models.DO_NOTHING, related_name='reservations')
    start_time = models.DateTimeField('Date Start', null=True, blank=True, db_index=True)
    end_time = models.DateTimeField('Date End', null=True, blank=True, db_index=True)
    participants_count = models.PositiveIntegerField('Number of Participants', default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f"{self.room} - Customer: {self.customers} - Date: {self.start_time} - {self.end_time} - Total number of participants: {self.participants_count}"   
    