from django.contrib import admin
from .models import *

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
