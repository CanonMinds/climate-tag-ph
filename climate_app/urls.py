from django.conf.urls import url
from . import views

app_name = "climate_app"

urlpatterns = [
    url(r"source-map/$", views.dashboard, name="source_map_dash"),
    url(
        r"climate-objective/$",
        views.dashboard,
        name="climate_objective_dash",
    ),
    url(
        r"sectoral-funding/$",
        views.dashboard,
        name="sectoral_funding_dash",
    ),
]
