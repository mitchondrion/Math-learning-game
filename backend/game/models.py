from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    GRADE_CHOICES = [
        (1, 'Grade 1'),
        (2, 'Grade 2'),
        (3, 'Grade 3'),
    ]
    grade = models.IntegerField(choices=GRADE_CHOICES)
    question_text = models.CharField(max_length=200)
    answer = models.FloatField()
    operator = models.CharField(max_length=1)  # +, -, *, /

    def __str__(self):
        return self.question_text

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return self.user.username

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.question.question_text}"