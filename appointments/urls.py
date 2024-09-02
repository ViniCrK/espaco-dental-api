from django.urls import path
from .views import AppointmentList, AppointmentDetail

app_name = 'appointments'

urlpatterns = [
    path('', AppointmentList.as_view()),
    path('<int:id>/', AppointmentDetail.as_view()),
]
