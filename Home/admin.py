from django.contrib import admin
from .models import Department
from .models import Doctor,Booking
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Booking)


# Register your models here.
