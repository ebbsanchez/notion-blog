from django.contrib import admin
from .models import Filter
# Register your models here.

@admin.register(Filter)
class FiltersAdmin(admin.ModelAdmin):
	pass