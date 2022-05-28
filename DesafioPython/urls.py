from django.contrib import admin
from django.urls import path
from Familiares.views import getFamilia;

urlpatterns = [
    path('admin/', admin.site.urls),
    path("familiares/", getFamilia)
]
