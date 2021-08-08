from django.contrib import admin

# Register your models here.
from climate_app.models import InitialModel
from climate_app.models import DACMemberCountry

class InitialModelAdmin(admin.ModelAdmin):
    list_display = ("sovereignty", "country_code", )
    search_fields = ("sovereignty",)

class DACMemberCountryAdmin(admin.ModelAdmin):
    list_display = ("provider", "year", "country_code", )
    search_fields = ("provider", "year", "country_code",)


admin.site.register(InitialModel, InitialModelAdmin)
admin.site.register(DACMemberCountry, DACMemberCountryAdmin)
