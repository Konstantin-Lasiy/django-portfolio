from django.shortcuts import render
from .models import Service, Project


def homepage(request):
    services = Service.objects.all()
    projects = Project.objects.order_by('-id')[:3]  # Get latest 3
    return render(request, 'homepage.html', {'services': services, 'projects': projects})
