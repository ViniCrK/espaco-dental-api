from django.urls import path
from .views import PatientList, PatientDetail, dentists_list, dentists_detail

app_name = 'users'

urlpatterns = [
    path('patients/', PatientList.as_view()),
    path('patients/<int:id>/', PatientDetail.as_view()),
    path('dentists/', dentists_list),
    path('dentists/<int:id>/', dentists_detail)
]
