from django import forms
from .models import Enrollment, CourseUnit
from users.models import customUser

class EnrollmentForm(forms.ModelForm):
    course_unit = forms.ModelChoiceField(queryset=CourseUnit.objects.all(), required=True)

    class Meta:
        model = Enrollment
        fields = ['course_unit']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(EnrollmentForm, self).__init__(*args, **kwargs)
        if user.is_student:
            self.fields['course_unit'].queryset = CourseUnit.objects.exclude(
                id__in=[e.course_unit.id for e in user.enrollment_set.all()]
            ).filter(course=user.course)
