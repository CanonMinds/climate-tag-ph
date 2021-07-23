from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>Climate App Dashboard Index. <br><br>It is now %s.</body></html>" % now
    return HttpResponse(html)

def dashboard(request):
    html = "<html><body>Climate App Contents.</body></html>"
    return HttpResponse(html)