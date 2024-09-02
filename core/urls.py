from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/users/', include('users.urls')),
    path('api/appointments/', include('appointments.urls')),
    path('admin/', admin.site.urls),
]
