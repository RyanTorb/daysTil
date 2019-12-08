from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.LoginView, name='login'),
    path('next/', views.temp, name='temp'),
    path('select/', views.Select, name='select'),
    path('add/',views.add,name='add'),
    path('del/<int:key>', views.delete, name='delete')
]