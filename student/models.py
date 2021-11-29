from django.db import models

# Create your models here.
class studentModel(models.Model):
    studentName = models.CharField(max_length=20)
    studentUsn = models.CharField(max_length=20)
    sem = models.CharField(max_length=20)

    def __str__(self):
        return self.studentUsn
