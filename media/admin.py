from django.contrib import admin
from .models import *


@admin.register(Video)
class AdAdmin(admin.ModelAdmin):

    # sortable_by = ['title', 'create_date', 'update_date']
    # list_filter = ['ad_type', 'advertiser']
    # search_fields = ['title']
    # fields = ['title', 'season', 'order', 'tag', 'album', 'person',]
    readonly_fields = ['create_at', 'update_at', ]
    exclude = ['create_at', 'update_at']
    list_display = ['title', 'create_at', 'update_at',]


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    readonly_fields = ['create_at', 'update_at']
    exclude = ['create_at', 'update_at']
    list_display = ['title', 'create_at', 'update_at',]


@admin.register(TVShow)
class TVShowAdmin(admin.ModelAdmin):
    readonly_fields = ['create_at', 'update_at']
    exclude = ['create_at', 'update_at']
    list_display = ['title', 'create_at', 'update_at',]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ['create_at', 'update_at']
    exclude = ['create_at', 'update_at']
    list_display = ['title', 'create_at', 'update_at',]


@admin.register(CollVideo)
class CollVideoAdmin(admin.ModelAdmin):
    readonly_fields = ['create_at', 'update_at']
    exclude = ['create_at', 'update_at']
    list_display = ['collection', 'video', 'create_at', 'update_at',]


@admin.register(Subtitle)
class SubtitleAdmin(admin.ModelAdmin):
    readonly_fields = ['create_at', 'update_at']
    exclude = ['create_at', 'update_at']
    list_display = ['video', 'language', 'create_at', 'update_at',]


@admin.register(Duble)
class DubleAdmin(admin.ModelAdmin):
    readonly_fields = ['create_at', 'update_at']
    exclude = ['create_at', 'update_at']
    list_display = ['video', 'language', 'create_at', 'update_at',]


@admin.register(People)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    exclude = ['created_at', 'updated_at']
    list_display = ['person', 'created_at', 'updated_at',]
