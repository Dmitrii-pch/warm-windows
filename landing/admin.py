from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'source', 'created_at')
    list_filter = ('source', 'created_at')
    search_fields = ('name', 'phone')
