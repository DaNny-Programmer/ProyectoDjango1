from django.shortcuts import render
from .models import Project
#create your views here.
def portfolio(request):
    projects= Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects':projects})