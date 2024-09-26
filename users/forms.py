from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import customUser, COURSE_CHOICES

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import customUser

COURSE_CHOICES = [
     ('BIS', 'Bachelor of Information Systems'),
    ('BITC', 'Bachelor of Information Techonology'),
    ('DCS', 'Diploma in Computer Science'),
]

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import customUser

COURSE_CHOICES = [
    ('BIS', 'Bachelor of Information Systems'),
    ('BITC', 'Bachelor of Information Techonology'),
    ('DCS', 'Diploma in Computer Science'),
]

class StudentSignupForm(UserCreationForm):
    sFirstName = forms.CharField(max_length=50, label="First Name")
    sMiddleName = forms.CharField(max_length=50, label="Middle Name", required=False)
    sLastName = forms.CharField(max_length=50, label="Last Name")
    regNo = forms.CharField(max_length=20, label="Registration Number")
    sNo = forms.CharField(max_length=20, label="Student Number")
    course = forms.ChoiceField(choices=COURSE_CHOICES, label="Course")
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(attrs={'id': 'email-input'}))
    
    class Meta(UserCreationForm.Meta):
        model = customUser
        fields = ('sFirstName', 'sMiddleName', 'sLastName', 'regNo', 'sNo', 'course', 'email', 'password1', 'password2')
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        if len(password1) < 8:
            raise ValidationError("Your password must contain at least 8 characters.")
        
        if password1.isdigit():
            raise ValidationError("Your password can’t be entirely numeric.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['sFirstName']  # Save the first name
        user.is_student = True
        user.username = self.cleaned_data['sFirstName'] + "" +  self.cleaned_data['sLastName']# Set username to sFirstName
        if commit:
            user.save()
        return user
    
    
class LecturerSignupForm(UserCreationForm):
    faculty_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(attrs={'id': 'email-input'}))

    class Meta(UserCreationForm.Meta):
        model = customUser
        fields = UserCreationForm.Meta.fields + ('faculty_name', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_lecturer = True
        user.faculty_name = self.cleaned_data['faculty_name']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)