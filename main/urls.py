from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bosh'),
    path('create', views.create, name='create'),
    path('about-us', views.about, name='about'),
]