from django.conf.urls import url
from . import views

app_name = "climate_app"

urlpatterns = [
    url(r"source-map/$", views.SourceMapView.as_view(), name="source_map_dash"),
    url(
        r"climate-objective/$",
        views.ClimateObjectiveView.as_view(),
        name="climate_objective_dash",
    ),
    url(
        r"sectoral-funding/$",
        views.SectoralFundingView.as_view(),
        name="sectoral_funding_dash",
    ),
]
