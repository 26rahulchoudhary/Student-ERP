from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StudentProfile
from courses.models import Enrollment

# Create your views here.

@login_required
def student_dashboard(request):
    user = request.user
    try:
        student_profile = StudentProfile.objects.get(user=user)
        enrollments = Enrollment.objects.filter(student=student_profile)
    except StudentProfile.DoesNotExist:
        student_profile = None
        enrollments = []
    return render(request, 'students/dashboard.html', {
        'student_profile': student_profile,
        'enrollments': enrollments,
    })
