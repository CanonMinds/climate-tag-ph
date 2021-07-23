from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    template_name = 'climate_app/dash_index.html'
    return render(request, template_name,  )

def dashboard(request):
    html = "<html><body>Climate App Contents.</body></html>"
    return HttpResponse(html)