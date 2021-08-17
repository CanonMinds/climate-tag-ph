"""django_root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from climate_app import views
import climate_app
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r"admin/", admin.site.urls, name="admin"),
    url(r"^$", TemplateView.as_view(template_name='site_construction.html'), name="site_index"),
    url(r"climate-app/", include("climate_app.urls", "climate_app")),
    url(r'^under-construction?$',
     TemplateView.as_view(template_name='site_construction.html'),
     name='construction'),
]
