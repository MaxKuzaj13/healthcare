from django.contrib import admin
from .models import Health


@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'created', 'modified']
