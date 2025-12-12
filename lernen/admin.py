from django.contrib import admin
from .models import Kategorie, Stufe, Karteikarte, UserKK

# Register your models here.

admin.site.register(Kategorie)
admin.site.register(Stufe)
admin.site.register(Karteikarte)
admin.site.register(UserKK)
