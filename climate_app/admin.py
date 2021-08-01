from django.contrib import admin

# Register your models here.
from climate_app.models import InitialModel

class InitialModelAdmin(admin.ModelAdmin):
    list_display = ('sovereignty', )
    search_fields = ('sovereignty', )

admin.site.register(InitialModel, InitialModelAdmin)