from django.urls import path
from . import views 

app_name = "Qrcode"

urlpatterns = [
    path('attendance/select_course_unit/', views.select_course_unit, name='select_course_unit'),
    path('attendance/select_course_unit_lecturer/', views.select_course_unit_lecturer, name='select_course_unit_lecturer'),
    path('attendance/select_lecture/<int:course_unit_id>/', views.select_lecture, name='select_lecture'),
    path('attendance/generate_qr/<int:lecture_id>/', views.generate_qr_code, name='generate_qr_code'),
    path('attendance/mark/<int:lecture_id>/', views.mark_attendance, name='mark_attendance'),
    path('attendance/scan_qr/<int:course_unit_id>/', views.scan_qr_code, name='scan_qr_code'),
]