from django.contrib import admin
from .models import employee
# Register your models here.

@admin.register(employee)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','salary','designation','company')