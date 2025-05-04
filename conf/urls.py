from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('core/', include('apps.core.urls', namespace='core')),
    path('api/', include('apps.api.urls', namespace='api')),
    path('customers/', include('apps.customers.urls', namespace='customers')),
    path('room/', include('apps.room.urls', namespace='room')),
    path('additional/', include('apps.additional.urls', namespace='additional')),
]
