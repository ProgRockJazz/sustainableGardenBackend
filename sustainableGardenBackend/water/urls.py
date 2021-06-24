from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('valves', views.ValveList.as_view()),
    path('valves/<int:pk>/', views.ValveDetail.as_view()),
    path('valves/<int:pk>/open/<double:time>', views.SensorRead.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
