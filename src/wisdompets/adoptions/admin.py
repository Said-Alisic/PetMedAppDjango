from django.contrib import admin

from .models import Pet

# Register model with admin
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']    

