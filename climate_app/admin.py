from django.contrib import admin

# Register your models here.
from climate_app.models import InitialModel
from climate_app.models import DACMemberCountry


class InitialModelAdmin(admin.ModelAdmin):
    list_display = (
        "sovereignty",
        "country_code",
    )
    search_fields = ("sovereignty",)


class DACMemberCountryAdmin(admin.ModelAdmin):
    list_display = (
        "provider",
        "sector",
        "channel_delivery",
        "year",
        "country_code",
        "is_published",
    )
    list_filter = (
        "adaptation_objective",
        "year",
        "is_published",
    )
    search_fields = (
        "provider",
        "year",
        "country_code",
    )


admin.site.register(InitialModel, InitialModelAdmin)
admin.site.register(DACMemberCountry, DACMemberCountryAdmin)
