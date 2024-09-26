from django.urls import path
from . import views 

app_name = "Qrcode"

urlpatterns = [
    path('select_course_unit/', views.select_course_unit, name='select_course_unit'),
    path('select_course_unit_lecturer/', views.select_course_unit_lecturer, name='select_course_unit_lecturer'),
    path('select_lecture/<int:course_unit_id>/', views.select_lecture, name='select_lecture'),
    path('generate_qr/<int:lecture_id>/', views.generate_qr_code, name='generate_qr_code'),
    path('mark/<int:lecture_id>/', views.mark_attendance, name='mark_attendance'),
    path('scan_qr/<int:course_unit_id>/', views.scan_qr_code, name='scan_qr_code'),
]