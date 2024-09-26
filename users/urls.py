from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path('signup/student/', views.student_signup, name='student_signup'),
    path('signup/lecturer/', views.lecturer_signup, name='lecturer_signup'),
    path('login/', views.user_login, name='login'),
    path('graphs/', views.graphs, name='graphs'),
    path('shared_reports/', views.shared_reports, name='shared_reports'),
    path('admin_view_report/<int:id>', views.admin_view_report, name='admin_view_report'),
    path('share_report/<str:id>', views.share_report, name='share_report'),
    path('graphs/lectures_in_unit/<int:code>/', views.lectures_in_unit, name='lectures_in_unit'),
    path('graphs/lectures_in_unit/plot_lecture/<str:name>', views.plot_attendance_graph, name='plot_lecture'),
    path('search/', views.search, name='search'),
    path('search/lectures_in_unit/<int:code>/', views.lectures_in_unit, name='lectures_in_unit'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('lecturer_dashboard/', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('landing/', views.landing, name='landing'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/verify/', views.password_reset_verify, name='password_reset_verify'),
    path('password_reset/confirm/', views.password_reset_confirm, name='password_reset_confirm'),
]