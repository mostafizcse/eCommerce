from django.contrib import admin

# Register your models here.
from .models import CustomarRegistration

# =========================================================================== Customar Register
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email']
    class Meta:
        model = CustomarRegistration
admin.site.register(CustomarRegistration, UserRegistrationAdmin)
