from django.shortcuts import render
from .models import Service, Project, Industry


def homepage(request):
    services = Service.objects.all()
    projects = Project.objects.order_by('-id')[:3]  # Get latest 3
    return render(request, 'services/home.html', {'services': services, 'projects': projects})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})


def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})


def about(request):
    return render(request, 'services/about.html')


def contact(request):
    return render(request, 'services/contact-us.html')


def industry_list(request):
    industries = Industry.objects.all()
    return render(request, 'services/industry_list.html', {'industries': industries})