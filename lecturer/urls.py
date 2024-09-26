from django.urls import path
from . import views 

app_name = "lecturer"

urlpatterns = [
path('create_course_unit/', views.create_course_unit, name='create_course_unit'),
path('create_lecture/', views.create_lecture, name='create_lecture'),
path('generate_attendance_report/<int:lecture_id>/', views.generate_attendance_report, name='generate_attendance_report'),
path('select_course_unit_for_report/', views.select_course_unit_for_report, name='select_course_unit_for_report'),
path('select_lecture_for_report/<int:course_unit_id>/', views.select_lecture_for_report, name='select_lecture_for_report'),
path('ajax/load-course-units/', views.load_course_units, name='load_course_units'),
path('generate_attendance_report_pdf/<int:lecture_id>/', views.generate_attendance_report_pdf, name='generate_attendance_report_pdf'),
    
]