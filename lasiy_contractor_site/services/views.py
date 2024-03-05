from django.shortcuts import render
from .models import Service, Project


def homepage(request):
    services = Service.objects.all()
    projects = Project.objects.order_by('-id')[:3]  # Get latest 3
    return render(request, 'services/home.html', {'services': services, 'projects': projects})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})


def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'service_detail.html', {'service': service})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

