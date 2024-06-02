from django.urls import path
from . import views  # из этой же директории мы вызываем представление

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
]
