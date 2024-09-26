# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


COURSE_CHOICES = [
    ('BIS', 'Bachelor of Information Systems'),
    ('BITC', 'Bachelor of Information Techonology'),
    ('DCS', 'Diploma in Computer Science'),
]

class customUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    regNo = models.CharField(max_length=15)
    sNo = models.CharField(max_length=20, blank=True, null=True)
    sFirstName = models.CharField(max_length=50, blank=True, null=True)
    sLastName = models.CharField(max_length=50, blank=True, null=True)
    sMiddleName = models.CharField(max_length=50, blank=True, null=True)
    faculty_name = models.CharField(max_length=100, blank=True, null=True)
    course = models.CharField(max_length=100, choices=COURSE_CHOICES, default='BIST')
    Staff_ID = models.CharField(max_length=15)
    
    def __str__(self):
        return self.username

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html',{'form':form})