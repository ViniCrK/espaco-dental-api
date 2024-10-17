from django.urls import path
from rest_framework.routers import DefaultRouter

from users import views

router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)
# router.register(r'dentists', views.DentistViewSet)

app_name = 'users'

urlpatterns = [
    # path('patients/', PatientList.as_view()),
    # path('patients/<int:id>/', PatientDetail.as_view()),
    path('dentists/', views.dentists_list),
    path('dentists/<int:id>/', views.dentists_detail)
] + router.urls
