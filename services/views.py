from django.shortcuts import render
from .models import Service, Project, Industry
import json
import os

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


def chart_test(request):
    data_file_path = os.path.join('services/static/services/data', 'aapl.json')
    with open(data_file_path, 'r') as file:
        data = json.load(file) 

    # Convert the Python dictionary to a JSON string to pass to the template
    data_json: str = json.dumps(data)
    print(data_json)
    return render(request, 'services/chart.html', {'aapl': data_json})

def chart_ridges(request):
    return render(request, 'services/chart-ridges.html')