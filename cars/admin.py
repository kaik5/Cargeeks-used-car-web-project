from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src= "{}" width = "40" style = "border-radius: 50px;" />'.format(object.photo.url))
    
    thumbnail.short_description = 'Photo'
    
    list_display = ( 'id', 'thumbnail' ,'car_title', 'year', 'model', 'color', 'condition', 'body_stlye', 'created_date', 'is_featured')
    list_display_links = ('id', 'car_title')
    search_fields = ('id', 'car_title', 'year', 'model', 'color', 'condition')
    list_editable = ('is_featured',)
    list_filter = ('id', 'car_title', 'city', 'model', 'color', 'condition', 'is_featured')
    
    
    
admin.site.register(Car, CarAdmin);