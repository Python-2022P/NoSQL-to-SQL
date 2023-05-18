from django.urls import path
from .views import smartphones,add_smartphone,get_smartphone, del_smartphone, upd_smartphone

urlpatterns = [
    path('smartphones/', smartphones),
    path('add/', add_smartphone),
    path('get/<int:id>', get_smartphone),
    path('del/<int:id>', del_smartphone),
    path('upd/<int:id>', upd_smartphone),
]
