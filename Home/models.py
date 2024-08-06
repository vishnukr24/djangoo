from django.db import models

# Create your models here.
class department(models.Model):
    dept_name = models.CharField(max_length=255)
    dept_description = models.TextField()
