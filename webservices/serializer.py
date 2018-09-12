from rest_framework import serializers
from bandas.models import *

class banda_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Banda
		fields =('url','nombre_banda', 'numero_integrantes','nacionalidad','photo')

class rol_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rol
		fields = ('url','nombre_rol')

class integrante_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Integrante
		fields = ('url','nombre','edad','genero','roles','direccion','banda','foto')

class nacionalidad_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Nacionalidad 
		fields = ('url','nombre_nacionalidad')