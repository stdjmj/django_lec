from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse
from django.shortcuts import render
from .models import MainContent


def index(request):
    #return HttpResponse("hello world")

    content_list = MainContent.objects.order_by("-pub_date")
    context = {"content_list": content_list}
    return render(request, "mysite/content_list.html", context)
