from django.urls import path
from . import views 

app_name = "student"

urlpatterns = [
    path('enroll/', views.enroll, name='enroll'),
    path('enroll/success/', views.enroll_success, name='enroll_success'),
]