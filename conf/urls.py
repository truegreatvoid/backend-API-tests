from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('core/', include('apps.core.urls', namespace='core')),
    path('api/', include('apps.api.urls', namespace='api')),
    path('customers/', include('apps.customers.urls', namespace='customers')),
    path('room/', include('apps.room.urls', namespace='room')),
    path('additional/', include('apps.additional.urls', namespace='additional')),
    path('office/', include('apps.office.urls', namespace='office')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
