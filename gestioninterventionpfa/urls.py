from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/',include("admins.urls")),
    path('accounts/', include("globals.urls")),
]
