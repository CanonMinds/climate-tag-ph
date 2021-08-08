from django.conf.urls import url
from . import views

app_name = "climate_app"

urlpatterns = [
    url(r"^$", views.SourceMapView.as_view(), name="climate_app_dashboard"),
]
