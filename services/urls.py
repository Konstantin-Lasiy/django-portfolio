from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact-us'),
    path('industries/', views.industry_list, name='industries'),
]

