from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins/',include("admins.urls")),
    path('accounts/', include("globals.urls")),
    path('clients/', include("clients.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
    ]
