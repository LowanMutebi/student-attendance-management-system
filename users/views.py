from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import customUser
from lecturer.models import Lecture, SharedReport
from .forms import StudentSignupForm, LecturerSignupForm
from student.models import Enrollment, CourseUnit
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.db.models import Q
from Qrcode.models import Attendance
from django.conf import settings
import random
from django.contrib import messages
from bokeh.plotting import figure
from bokeh.embed import components
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

# Create your views here.
def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:student_dashboard')
    else:
        form = StudentSignupForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'Student'})

def lecturer_signup(request):
    if request.method == 'POST':
        form = LecturerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:lecturer_dashboard')
    else:
        form = LecturerSignupForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'Lecturer'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_student:
                return redirect('users:student_dashboard')
            elif user.is_lecturer:
                return redirect('users:lecturer_dashboard')
        else:
           messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def student_dashboard(request):
    page_title = "student_dashboard"
    student = request.user
    enrolled_units = Enrollment.objects.filter(student=student)
    return render(request, 'student_dashboard.html',{'page_title': page_title, 'enrolled_units': enrolled_units })

@login_required
def lecturer_dashboard(request):
    page_title = "lecture's dashboard"
    created_courseunits = CourseUnit.objects.filter(lecturer=request.user)
    return render(request, 'lecturer_dashboard.html',{'page_title': page_title, 'created_courseunits': created_courseunits})

def landing(request):
    page_title = "Home"
    return render(request, 'landing.html', {'page_title': page_title})

def logout_view(request):
    logout(request)
    return redirect('users:landing')


def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = customUser.objects.filter(email=email).first()
        if user:
            random_code = random.randint(100000, 999999)
            request.session['reset_code'] = random_code
            request.session['reset_email'] = email
            send_mail(
                'Password Reset Code',
                f'Dear {user.username},\n\n'
                f'We received a request to reset the password for your account associated with this email address. If you made this request, please use the verification code provided below to reset your password.\n\n'
                f'Your password reset code is: {random_code}\n\n'
                f'If you did not request a password reset, please ignore this email. Your account remains secure, and no changes have been made.\n\n'
                f'Thank you,\n'
                f'The Student Attendance System Team',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return redirect('users:password_reset_verify')
    return render(request, 'registration/password_reset_request.html')


def password_reset_verify(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if code == str(request.session.get('reset_code')):
            return redirect('users:password_reset_confirm')
        else:
            return render(request, 'registration/password_reset_verify.html', {'error': 'Invalid code'})
    return render(request, 'registration/password_reset_verify.html')


def password_reset_confirm(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.session.get('reset_email')
        user = customUser.objects.filter(email=email).first()
        if user:
            user.set_password(password)
            user.save()
            return redirect('users:login')
    return render(request, 'registration/password_reset_confirms.html')

@login_required
def graphs(request):
    course_units = CourseUnit.objects.all()
    return render(request, 'graphs.html', {'course_units': course_units, 'course_unit':True})

@login_required
def shared_reports(request):
    reports = SharedReport.objects.all()
    return render(request, 'shared_reports.html', {'reports': reports})

@login_required
def search(request):
    query = request.GET.get('search')
    course_units = CourseUnit.objects.filter(Q(code__icontains=query) | Q(course__icontains=query) | Q(lecturer__username__icontains=query))
    return render(request, 'graphs.html', {'course_units': course_units, 'course_unit':True})

@login_required
def lectures_in_unit(request, code):
    lectures_titles = []
    lectures_front_end = []
    lectures = Lecture.objects.filter(course_unit=code)  
    for lecture in lectures:
        if str(lecture.title) not in lectures_titles:
            lectures_titles.append(str(lecture.title))
            lectures_front_end.append(lecture)
    return render(request, 'graphs.html', {'course_units': lectures_front_end, 'course_unit':False})

@login_required
def plot_attendance_graph(request, name):
    attendance = Attendance.objects.filter(lecture__title=name)
    attendance_dates = Attendance.objects.filter(lecture__title=name).values_list('date', flat=True)
    # Calculate aggregate attendance on each day
    attendance_count = attendance.values('date').annotate(total_attendance=models.Count('id'))
    # Prepare data for plotting
    dates = list(set([str(date) for date in attendance_dates]))
    counts = [count['total_attendance'] for count in attendance_count]
    return render(request, 'graphs.html', {'plot': True,  'labels': dates, 'data': counts})

@login_required
def admin_view_report(request, id):
    lecture = Lecture.objects.get(id=id)
    print(lecture)
    course_unit = lecture.course_unit
    enrolled_students = Enrollment.objects.filter(course_unit=course_unit).values_list('student', flat=True)
    students = User.objects.filter(id__in=enrolled_students)

    
    attendance_records = Attendance.objects.filter(lecture=lecture)

    
    report = []
    for student in students:
        full_name = " ".join(filter(None, [student.sFirstName, student.sLastName]))
        attendance_record = attendance_records.filter(student=student).first()
        if attendance_record:
            status = attendance_record.status
        else:
            status = 'absent'
        print(report)
        report.append({
            'full_name': full_name,
            'regNo': student.regNo,
            'sNo': student.sNo,
            'status': status
        })

    return render(request, 'admin_view_report.html', {
        'lecture': lecture,
        'report': report
    })

@login_required
def share_report(request, id):
    lecture_id = id
    lecture = Lecture.objects.get(id=id)
    report = SharedReport(lecture=lecture, uploaded_by=request.user)
    report.save()
    messages.success(request, 'Report shared successfully')
    if request.user.is_lecturer:
        lecture = get_object_or_404(Lecture, id=lecture_id, course_unit__lecturer=request.user)
        course_unit = lecture.course_unit
        
        enrolled_students = Enrollment.objects.filter(course_unit=course_unit).values_list('student', flat=True)
        students = User.objects.filter(id__in=enrolled_students)

       
        attendance_records = Attendance.objects.filter(lecture=lecture)

       
        report = []
        for student in students:
            full_name = " ".join(filter(None, [student.sFirstName, student.sLastName]))
            attendance_record = attendance_records.filter(student=student).first()
            if attendance_record:
                status = attendance_record.status
            else:
                status = 'absent'
            print(report)
            report.append({
                'full_name': full_name,
                'regNo': student.regNo,
                'sNo': student.sNo,
                'status': status
            })

        return render(request, 'generate_attendance_report.html', {
            'lecture': lecture,
            'report': report
        })
    else:
        return redirect('users:lecturer_dashboard')