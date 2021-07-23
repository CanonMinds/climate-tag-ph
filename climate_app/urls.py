from django.conf.urls import url
from . import views

app_name = 'climate_app'

urlpatterns = [
    url(r'^$', views.dashboard, name='climate_app_dashboard'),
]