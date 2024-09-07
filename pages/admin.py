from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):#to display picture
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))
    
    thumbnail.short_description = 'photo'#changing the name thumbnail to photo
    
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date')#this is a tuple
    list_display_links = ('id', 'thumbnail', 'first_name',)#to be clickable
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)