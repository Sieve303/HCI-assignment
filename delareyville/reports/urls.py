from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report, name='report'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('check-login/', views.check_login, name='check_login'),
    path('track-report/', views.track_report, name='track_report'),
    path('logout/', views.logout, name='logout'),
]
