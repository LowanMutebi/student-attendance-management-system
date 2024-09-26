from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EnrollmentForm
# Create your views here.

@login_required
def enroll(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, user=request.user)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = request.user
            enrollment.save()
            return redirect('student:enroll_success')
    else:
        form = EnrollmentForm(user=request.user)
    return render(request, 'enroll.html', {'form': form})

@login_required
def enroll_success(request):
    return render(request, 'enroll_success.html')