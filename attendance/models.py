from django.db import models

# Create your models here.

class Attendance(models.Model):
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    class Meta:
        unique_together = ('student', 'course', 'date')

    def __str__(self):
        return f"{self.student} - {self.course} - {self.date} - {self.status}"
