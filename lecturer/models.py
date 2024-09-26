from django.db import models
from student.models import CourseUnit
from users.models import customUser
import datetime
# Create your models here.

class Lecture(models.Model):
    course_unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(default=datetime.time(9, 0))  # Default time set to 9:00 AM
    duration = models.DurationField(default=datetime.timedelta(hours=2))  # Default duration set to 1 hour
    latitude = models.FloatField(default=0.3324)
    longitude = models.FloatField(default=32.5705)    

    def __str__(self):
        return self.title    
    
class SharedReport(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(customUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.lecture.title