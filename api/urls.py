from django.urls import path
from .views import smartphones

urlpatterns = [
    path('smartphones/', smartphones),
]
