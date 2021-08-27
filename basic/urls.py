from django.urls import path
from basic import views

urlpatterns = [
    path('', views.home),
    path('info/', views.info),
    path('contactus/', views.contactus),
    path('carousel/', views.carousel),
]
