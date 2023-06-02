from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('files_section', views.files_section, name='files_section'),
    path('admin', views.admin, name='admin'),
]