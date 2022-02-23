
from django.db import models

class CourseOffering(models.Model):
    time = models.TimeField('time duration')    
    secno = models.IntegerField()
    room = models.CharField(max_length=10)
    sem = models.CharField(max_length=10)
    course_code = models.CharField(max_length=150)
    def __str__(self):
        return self.course_code


class Student(models.Model):
    name = models.CharField(max_length=50)
    program = models.CharField(max_length=150)
    course = models.ForeignKey(CourseOffering,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=150)
    time = models.DateTimeField('date and time')    

    def __str__(self):
        return self.name


class Takes(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courseoffer = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField()                                                                                                                                                   

    def __str__(self):
        return f'{self.student} {self.exam} {self.courseoffer} {self.marks}'