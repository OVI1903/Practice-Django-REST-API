from django.contrib import admin
from .models import Test_member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("Member_Name", "Age", "Address",)
    
    admin.site.register(Test_member)