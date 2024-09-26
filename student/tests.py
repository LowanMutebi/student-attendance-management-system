from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Enrollment, CourseUnit

# Create your tests here.


class EnrollmentTests(TestCase):

    def setUp(self):
        self.student = get_user_model().objects.create_user(
            username='student1', password='testpassword', email='student1@example.com', 
            is_student=True, course='Computer Science')
        self.course_unit = CourseUnit.objects.create(name='Data Structures', code='CS101', 
        course='Computer Science', lecturer_id=1)
        self.client.login(username='student1', password='testpassword')

    def test_enroll_in_course_unit(self):
        response = self.client.post(reverse('student:enroll'), {'course_unit': self.course_unit.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Enrollment.objects.filter(student=self.student, course_unit=self.course_unit).exists())
        print("Test `test_enroll_in_course_unit` passed.")
