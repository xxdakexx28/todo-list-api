from django.contrib import admin
from .models import todos


# Register your models here.

class todoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(todos, todoAdmin)