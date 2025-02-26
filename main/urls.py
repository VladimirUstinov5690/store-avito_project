from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('webhook/', views.get_data, name='get_data'),
]
