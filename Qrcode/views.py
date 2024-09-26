from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import qrcode
from io import BytesIO
from django.http import JsonResponse, HttpResponse
from .models import Lecture, Attendance
from student.models import CourseUnit, customUser, Enrollment
import math
from datetime import datetime, timedelta



# Create your views here.


# Function to calculate the distance between two points (latitude, longitude)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon1 - lon2)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
    


@login_required
def generate_qr_code(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    url = request.build_absolute_uri(f'/attendance/mark/{lecture_id}/')
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')


@login_required
def mark_attendance(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    student = request.user  
    if student.is_student:

        if Attendance.objects.filter(student=student, lecture=lecture,status='present').exists():
            return JsonResponse({'status': 'error', 'message': 'Attendance already marked for this lecture.'})
        
        student_id = student.id
        student_lat = float(request.GET.get('latitude'))
        student_lon = float(request.GET.get('longitude'))

        # Log user ID and location for debugging,status='present'
        print(f"Student ID: {student_id}, Latitude: {student_lat}, Longitude: {student_lon}")

        lecture_lat = lecture.latitude
        lecture_lon = lecture.longitude

        # Check if the student is within 100 meters of the lecture location
        distance = haversine(student_lat, student_lon, lecture_lat, lecture_lon)
        now = timezone.now()

        # Validate the lecture time and duration
        lecture_start_datetime = timezone.make_aware(datetime.combine(lecture.date, lecture.start_time))
        lecture_end_datetime = lecture_start_datetime + lecture.duration
        if now > lecture_end_datetime:
            return JsonResponse({'status': 'error', 'message': 'Lecture has ended. Attendance cannot be marked.'})

        if distance <= 14:  #  km = 100 meters
            Attendance.objects.create(student=student, lecture=lecture, date=timezone.now().date(),status='present')
            return JsonResponse({'status': 'success', 'message': 'Attendance marked successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': f'Absent, you are not in the lecture room. Distance: {distance:.2f} km'})
    return JsonResponse({'status': 'error', 'message': 'Only students can mark attendance'})



@login_required
def select_course_unit(request):
    student = request.user
    enrolled_units = Enrollment.objects.filter(student=student)
    return render(request, 'select_course_unit.html', {'enrolled_units': enrolled_units})

def select_course_unit_lecturer(request):
    lecturer = request.user
    created_units = CourseUnit.objects.filter(lecturer=lecturer)
    return render(request, 'select_course_unit_lecturer.html', {'created_units': created_units})


@login_required
def select_lecture(request, course_unit_id):
    course_unit = get_object_or_404(CourseUnit, id=course_unit_id)
    lectures = Lecture.objects.filter(course_unit=course_unit)
    return render(request, 'select_lecture.html', {'lectures': lectures, 'course_unit': course_unit})

@login_required
def scan_qr_code(request, course_unit_id):
    lectures = Lecture.objects.filter(course_unit_id=course_unit_id)
    return render(request, 'scan_qr_code.html', {'lectures': lectures})