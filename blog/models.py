from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    


class Posteo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete= models.PROTECT, default = 1)
    # autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    
    
    
class Comentarios(models.Model):
    posteo = models.ForeignKey(Posteo, on_delete=models.CASCADE, related_name = 'comentarios')
    nombre = models.CharField(max_length=50)
    contenido = models.TextField()