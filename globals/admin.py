from django.contrib import admin
from .models import*
from leaflet.admin import LeafletGeoAdmin



admin.site.register(Intervention)
admin.site.register(Technicien)
admin.site.register(Client)
admin.site.register(Admin)