from django.db import models

# Create your models here.

class Result(models.Model):
    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    marks = models.FloatField()

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} - {self.course}: {self.marks}"
