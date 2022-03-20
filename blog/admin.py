from django.contrib import admin

from blog.models import Categoria, Comentarios, Posteo

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Posteo)
admin.site.register(Comentarios)