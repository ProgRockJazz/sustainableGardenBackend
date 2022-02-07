from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from loginAndRegisterUsers import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserList)

urlpatterns = [
    path('', include(router.urls)),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]
