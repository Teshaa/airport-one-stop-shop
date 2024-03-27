from django.contrib import admin

from core.models import Service, Terminal

# Register your models here.

@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")