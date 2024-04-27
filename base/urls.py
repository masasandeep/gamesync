from django.urls import path,include
from .views import home,gaming_profile
urlpatterns = [
    path('',home,name='home'),
    path('gaming_profile/<str:pk>/',gaming_profile,name='gaming-profile')
]