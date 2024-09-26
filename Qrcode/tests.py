from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Attendance, Lecture
from student.models import CourseUnit
from django.utils import timezone
from datetime import datetime, timedelta
# Create your tests here.


class AttendanceTests(TestCase):

    def setUp(self):
        self.student = get_user_model().objects.create_user(
            username='student1', password='testpassword', email='student1@example.com', is_student=True, 
            course='BCS')
        self.lecturer = get_user_model().objects.create_user(
            username='lecturer1', password='testpassword', email='lecturer1@example.com', is_lecturer=True)
        self.course_unit = CourseUnit.objects.create(name='Data Structures', code='CS101', course='BCS', 
        lecturer=self.lecturer)
        self.lecture = Lecture.objects.create(course_unit=self.course_unit, title='Introduction to Data Structures',
        date=timezone.now().date(), start_time=timezone.now().time(), 
        duration=timedelta(hours=2), latitude=0.3329, longitude=32.5831)
        self.client.login(username='student1', password='testpassword')

    def test_mark_attendance(self):
        response = self.client.get(reverse('Qrcode:mark_attendance', args=[self.lecture.id]) 
            + '?latitude=0.3329&longitude=32.5831')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Attendance.objects.filter(student=self.student, lecture=self.lecture).exists())
        print("Test `AttendanceTests` passed.")
