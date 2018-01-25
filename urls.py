from django.urls import path
from . import views

app_name = 'ifsearch'
urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.search, name='query'),
]
