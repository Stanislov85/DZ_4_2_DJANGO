from django.contrib import admin
from django.urls import path
from .views import recept_view, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('<recept>/', recept_view, name='recept'),
    path('admin/', admin.site.urls),
]

