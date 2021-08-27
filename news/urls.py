from django.urls import path
from news import views

urlpatterns = [
    path('list/', views.list_),
    path('detail/', views.detail),
    path('detail_page/', views.detail_page),
    path('list_page/', views.list_page),
]
