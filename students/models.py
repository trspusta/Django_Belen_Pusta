from django.db import models

# Create your models here.
class Students(models.Model):
    full_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    grades = models.CharField(max_length=50)
    age = models.FloatField()

    def __str__(self):
        return f'Student: {self.full_name}'
    

