from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admins/',include("admins.urls")),

    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
]
