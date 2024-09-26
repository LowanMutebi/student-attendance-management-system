from django.test import TestCase
from django.urls import reverse
from .models import customUser
from .forms import StudentSignupForm, LecturerSignupForm
from django.core import mail
from django.contrib.auth import get_user_model
# Create your tests here.


class UserRegistrationTests(TestCase):

    def test_student_signup(self):
        response = self.client.post(reverse('users:student_signup'), {
            'username': 'student1',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'student1@example.com',
            'regNo': '123456',
            'course': 'BCS'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(customUser.objects.filter(username='student1').exists())
        print("Test `test_student_signup` passed.")

    def test_lecturer_signup(self):
        response = self.client.post(reverse('users:lecturer_signup'), {
            'username': 'lecturer1',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'lecturer1@example.com',
            'faculty_name': 'Engineering'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(customUser.objects.filter(username='lecturer1').exists())
        print("Test `test_lecturer_signup` passed.")




class PasswordResetTests(TestCase):

    def setUp(self):
        self.student = get_user_model().objects.create_user(
            username='student1', password='testpassword', email='student1@example.com', is_student=True, course='BSC')

    def test_password_reset_request(self):
        response = self.client.post(reverse('users:password_reset'), {'email': 'student1@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        print("Test `PasswordResetTests` passed.")

    def test_password_reset_verify(self):
        self.client.post(reverse('users:password_reset'), {'email': 'student1@example.com'})
        reset_code = self.client.session['reset_code']
        response = self.client.post(reverse('users:password_reset_verify'), {'code': reset_code})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:password_reset_confirm'))
        print("Test `test_password_reset_verify` passed.")

    def test_password_reset_confirm(self):
        self.client.post(reverse('users:password_reset'), {'email': 'student1@example.com'})
        reset_code = self.client.session['reset_code']
        self.client.post(reverse('users:password_reset_verify'), {'code': reset_code})
        response = self.client.post(reverse('users:password_reset_confirm'), {'password': 'newpassword'})
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertTrue(self.student.check_password('newpassword'))
        print("Test `test_password_reset_confirm` passed.")
