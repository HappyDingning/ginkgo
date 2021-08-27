from django.urls import path
from . import views

urlpatterns = [
    path('achievement/', views.achievement_),
    path('list/', views.members_list),
    path('member_detail/', views.member_detail),
    path('member_detail_page/', views.member_detail_page),
    path('achievement_page/', views.achievement_page),
    path('list_page/', views.list_page),
]
