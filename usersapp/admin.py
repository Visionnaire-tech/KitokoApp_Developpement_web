from django.contrib import admin
from .models import Classe ,Promotion,Vacation,EnvoisTp,Faculty,Cursus
# Register your models here.

admin.site.register(Classe)
admin.site.register(Promotion)
admin.site.register(Vacation)
admin.site.register(EnvoisTp)
admin.site.register(Faculty)
admin.site.register(Cursus)