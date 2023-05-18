from django.urls import path
from .views import smartphones,add_smartphone,get_smartphone

urlpatterns = [
    path('smartphones/', smartphones),
    path('add/', add_smartphone),
    path('get/<id>', get_smartphone),
]