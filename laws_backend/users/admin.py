from django.contrib import admin
from .models import *

# Register your models here.
admin.register(User, UserProfile,
               Role, UserRole)
