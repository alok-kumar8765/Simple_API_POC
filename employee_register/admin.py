from django.contrib import admin

# Register your models here.
from . models import Employee,Position
admin.site.register(Employee)
admin.site.register(Position)