from django.contrib import admin

from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['First_Name', 'Last_Name', 'Phone_Number','Address',]
    
admin.site.register(Employee, EmployeeAdmin)