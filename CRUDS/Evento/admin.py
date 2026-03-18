from django.contrib import admin
from . import models 
# Register your models here.

admin.site.register(models.Evento)
admin.site.site_header = "Gastro Bar"
admin.site.site_title = "Agora - Admin "
admin.site.index_title = "Bienvenido"