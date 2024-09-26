from django.db import models
from users.models import customUser
from lecturer.models import Lecture
# Create your models here.

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]
    student = models.ForeignKey(customUser, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='absent')

    def __str__(self):
        return f'{self.student.username} attended {self.lecture.title} on {self.date}'