from django.contrib import admin
from .models import Service, Blog  # Make sure Blog is imported

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # Automatically generate the slug from the name
    list_display = ('name', 'order')
    ordering = ('order',)
    list_editable = ('order',)
    
    # Add benefits and how_it_works to the form in the admin interface
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'icon', 'order')
        }),
        ('Additional Information', {
            'fields': ('benefits', 'how_it_works'),
        }),
    )

# Registering the Blog model in the admin
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # Automatically generate the slug from the title
    list_display = ('title', 'author', 'publish_date', 'read_time')
    search_fields = ('title', 'content', 'author')  # Allows searching by title, content, and author
    list_filter = ('publish_date', 'author')  # Filters for author and publish date
    date_hierarchy = 'publish_date'  # Adds a date-based drilldown navigation
    ordering = ('-publish_date',)  # Orders by publish date descending
