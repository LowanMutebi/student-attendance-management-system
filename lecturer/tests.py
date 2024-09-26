from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from student.models import CourseUnit

# Create your tests here.


class CourseUnitTests(TestCase):

    def setUp(self):
        self.lecturer = get_user_model().objects.create_user(
            username='lecturer1', password='testpassword', email='lecturer1@example.com', is_lecturer=True)
        self.client.login(username='lecturer1', password='testpassword')

    def test_create_course_unit(self):
        response = self.client.post(reverse('lecturer:create_course_unit'), {
            'name': 'Data Structures',
            'code': 'CS101',
            'course': 'BCS'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CourseUnit.objects.filter(name='Data Structures').exists())
        print("Test `test_create_course_unit` passed.")