from django.db import models

class Livros(models.Model):
    class Meta:
        db_table = 'livros'
        
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    anoLancamento = models.IntegerField()