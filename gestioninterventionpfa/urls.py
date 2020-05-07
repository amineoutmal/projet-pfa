from django.contrib import admin
from django.urls import path,include

urlpatterns = [
<<<<<<< HEAD
    path('admins/',include("admins.urls")),

=======
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
>>>>>>> d2b816c9861db44a93e1722ed3d19c36d814f10c
]
