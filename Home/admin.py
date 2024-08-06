from django.contrib import admin
from . models import department, Doctor, Booking
# Register your models here.
admin.site.register(department)
admin.site.register(Doctor)
admin.site.register(Booking)