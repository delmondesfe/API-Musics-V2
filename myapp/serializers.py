from rest_framework import serializers
from .models.musicDTO import Music
from .models.livrosDTO import Livros

class MusicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Music
        fields = '__all__'
        
class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'
        