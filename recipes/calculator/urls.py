from django.contrib import admin
from django.urls import path
from .views import omlet_view, pasta_view, buter_view, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('omlet/', omlet_view, name='omlet'),
    path('pasta/', pasta_view, name='pasta'),
    path('buter/', buter_view, name='buter'),
    path('admin/', admin.site.urls),
]

