
from django import forms
from .models import CourseUnit, Lecture
from django.forms.widgets import DateInput
from .models import Lecture
from student.models import CourseUnit, COURSE_CHOICES
from datetime import datetime
from django.utils import timezone
from student.models import CourseUnit, COURSE_CHOICES,COURSE_UNIT_CHOICES

class CourseUnitForm(forms.ModelForm):
    course = forms.ChoiceField(choices=[('', 'Select a course...')] + COURSE_CHOICES)
    code = forms.ChoiceField(choices=[('', 'Select a course unit...')]+[(code, name) for code, name, _ in COURSE_UNIT_CHOICES])

    class Meta:
        model = CourseUnit
        fields = ['course', 'code']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['course_unit', 'title', 'date', 'start_time', 'duration', 'latitude', 'longitude']

    def __init__(self, *args, **kwargs):
        
        lecturer = kwargs.pop('lecturer', None)
        super(LectureForm, self).__init__(*args, **kwargs)
        self.fields['course_unit'].queryset = CourseUnit.objects.filter(lecturer=lecturer)
        self.fields['date'].widget = forms.DateInput(attrs={'class': 'form-control datepicker'})
        self.fields['start_time'].widget.attrs.update({'class': 'form-control timepicker'})
        
        if lecturer:
            
         self.fields['course_unit'].queryset = CourseUnit.objects.filter(lecturer=lecturer)
        self.fields['date'].widget = forms.DateInput(attrs={'class': 'form-control datepicker'})
        self.fields['start_time'].widget = forms.TimeInput(attrs={'class': 'form-control timepicker'})
        self.fields['duration'].widget.attrs.update({'class': 'form-control'})
        self.fields['latitude'].widget.attrs.update({'class': 'form-control', 'id': 'id_latitude'})
        self.fields['longitude'].widget.attrs.update({'class': 'form-control', 'id': 'id_longitude'})

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        
        if start_time < timezone.now().time():
            raise forms.ValidationError("Start time cannot be in the past.")
        # Ensure date is in the future
        data = self.cleaned_data['date']
        if data < date.today():
            raise forms.ValidationError("Select a date that is today or in the future.")

        return cleaned_data