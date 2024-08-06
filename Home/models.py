from django.db import models

# Create your models here.
class department(models.Model):
    dept_name = models.CharField(max_length=255)
    dept_description = models.TextField()


    def __str__(self):
        return self.dept_name
    

class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_specialisation = models.TextField()
    dept_name = models.ForeignKey(department, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors', blank=True, null=True)

    def __str__(self) -> str:
        return self.doc_name
    

class Booking(models.Model):
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=100)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.p_name
    