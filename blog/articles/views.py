from django.shortcuts import render
from datetime import datetime
#from django.http import HttpResponse

from .models import Article

# Create your views here.

def homepage(request):
    return render(request, "articles/homepage.html", {
        "d": datetime.now(),
        "articles": Article.objects.filter()
    })

#def homepage(request):
#    return HttpResponse("hurra! dziala")
