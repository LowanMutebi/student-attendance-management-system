from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lecture
from .forms import CourseUnitForm, LectureForm
from student.models import CourseUnit
from Qrcode.models import Attendance
from django.utils import timezone 

from django.http import JsonResponse
from student.models import CourseUnit, COURSE_UNIT_CHOICES
from django.urls import reverse

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from student.models import Enrollment

# Create your views here.
@login_required
def create_course_unit(request):
    if request.user.is_lecturer:
        if request.method == 'POST':
            form = CourseUnitForm(request.POST)
            if form.is_valid():
                course_unit = form.save(commit=False)
                course_unit.lecturer = request.user
                course_unit.save()
                return redirect('users:lecturer_dashboard')
            else:
                print(form.errors)
        else:
            form = CourseUnitForm()
        return render(request, 'create_course_unit.html', {'form': form})
    else:
        return redirect('users:lecturer_dashboard')
        
    
@login_required
def create_lecture(request):
    if request.user.is_lecturer:
        if request.method == 'POST':
            form = LectureForm(request.POST, lecturer=request.user)
            if form.is_valid():
                lecture = form.save(commit=False)
                lecture.save()
                
                qr_code_url = reverse('Qrcode:generate_qr_code', args=[lecture.id])
                
                return redirect("users:lecturer_dashboard")
        else:
            form = LectureForm(lecturer=request.user)
            
        return render(request, 'create_lecture.html', {'form': form})
    else:
        return redirect('users:lecturer_dashboard')
    

def load_course_units(request):
    course = request.GET.get('course')
    lecturer_id = request.GET.get('lecturer_id')
    print('Received course:', course)  # Debugging line
    print('Lecturer ID:', lecturer_id)  # Debugging line

    existing_course_units = CourseUnit.objects.filter(course=course, lecturer_id=lecturer_id).values_list('code', flat=True)
    print('Existing course units:', existing_course_units)  # Debugging line

    filtered_course_units = [
        {'code': code, 'name': name}
        for code, name, course_code in COURSE_UNIT_CHOICES
        if course_code == course and code not in existing_course_units
    ]
    print('Filtered course units:', filtered_course_units)  # Debugging line
    return JsonResponse(filtered_course_units, safe=False)
    
    
@login_required
def select_course_unit_for_report(request):
    if request.user.is_lecturer:
        if request.method == 'POST':
            course_unit_id = request.POST.get('course_unit')
            return redirect('lecturer:select_lecture_for_report', course_unit_id=course_unit_id)

        course_units = CourseUnit.objects.filter(lecturer=request.user)
        return render(request, 'select_course_unit_for_report.html', {'course_units': course_units})
    else:
        return redirect('users:lecturer_dashboard')

@login_required
def select_lecture_for_report(request, course_unit_id):
    if request.user.is_lecturer:
        course_unit = get_object_or_404(CourseUnit, id=course_unit_id, lecturer=request.user)
        lectures = Lecture.objects.filter(course_unit=course_unit)

        if request.method == 'POST':
            lecture_id = request.POST.get('lecture')
            return redirect('lecturer:generate_attendance_report', lecture_id=lecture_id)

        return render(request, 'select_lecture_for_report.html', {'course_unit': course_unit, 'lectures': lectures})
    else:
        return redirect('users:lecturer_dashboard')

User = get_user_model()

@login_required
def generate_attendance_report(request, lecture_id):
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
    


@login_required
def generate_attendance_report_pdf(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id, course_unit__lecturer=request.user)
    course_unit = lecture.course_unit

    # Get all students enrolled in the course unit
    enrolled_students = Enrollment.objects.filter(course_unit=course_unit).values_list('student', flat=True)
    students = User.objects.filter(id__in=enrolled_students)

    # Get attendance records for the lecture
    attendance_records = Attendance.objects.filter(lecture=lecture)

    # Create a list of students with their attendance status
    report = []
    for student in students:
        full_name = " ".join(filter(None, [student.sFirstName, student.sMiddleName, student.sLastName]))
        attendance_record = attendance_records.filter(student=student).first()
        if attendance_record:
            status = attendance_record.status
        else:
            status = 'absent'
        report.append({
            'full_name': full_name,
            'regNo': student.regNo,
            'sNo': student.sNo,
            'status': status
        })

    template_path = 'attendance_report_pdf.html'
    context = {
        'lecture': lecture,
        'report': report
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="attendance_report_{lecture.id}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors with code %s' % pisa_status.err, status=400)
    return response