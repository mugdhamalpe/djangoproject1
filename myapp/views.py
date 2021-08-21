from django.shortcuts import render
from django.http import HttpResponse
from .models import Domains

# Create your views here.

def index(request):
    return HttpResponse("hello world!")

def domains_by_id(request, domains_id):
    domains = Domains.objects.get(pk=domains_id)
    return render(request, 'index.html', {'domains':domains})