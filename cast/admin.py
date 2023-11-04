from django.contrib import admin
from .models import *


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    # sortable_by = ['title', 'create_date', 'update_date']
    # list_filter = ['ad_type', 'advertiser']
    # search_fields = ['title']
    # fields = ['title', 'ad_type', 'advertiser', 'media', 'content']
    readonly_fields = ['created_at', 'updated_at']
    exclude = ['created_at', 'updated_at']
    list_display = ['first_name', 'last_name', 'created_at', 'updated_at',]
