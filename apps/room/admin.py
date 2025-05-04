from django.contrib import admin

from apps.room.models import Room, Reservation

admin.site.register(Room)
admin.site.register(Reservation)