from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('sensors/', views.SensorList.as_view()),
    path('sensors/<int:pk>/', views.SensorDetail.as_view()),
    path('sensors/<int:pk>/read', views.SensorRead.as_view()),
    path('sensors/all/read/', views.SensorReadAll.as_view()),
    path('sensors/readings/', views.SensorReadingList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
