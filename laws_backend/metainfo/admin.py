from django.contrib import admin
from .models import *

# Register your models here.
admin.register(Setting, DocumentTemplate,
               ErrorDescription, Info,
               SystemMessage)