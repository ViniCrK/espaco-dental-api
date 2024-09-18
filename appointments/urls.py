from django.urls import path
from rest_framework.routers import DefaultRouter

from appointments import views

router = DefaultRouter()
router.register(r'', views.AppointmentViewSet)

app_name = 'appointments'

urlpatterns = [
    # path('', AppointmentList.as_view()),
    # path('<int:id>/', AppointmentDetail.as_view()),
] + router.urls
