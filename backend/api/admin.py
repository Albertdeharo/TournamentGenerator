from django.contrib import admin
from .models import Company
from .models import Tournament

# Register your models here.

admin.site.register(Company)
admin.site.register(Tournament)