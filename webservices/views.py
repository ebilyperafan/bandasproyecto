from django.shortcuts import render
from bandas.models import *
from .serializer import *
from rest_framework import viewsets

# Create your views here.

class banda_viewset(viewsets.ModelViewSet):
	queryset = Banda.objects.all()
	serializer_class = banda_serializer

class rol_viewset(viewsets.ModelViewSet):
	queryset = Rol.objects.all()
	serializer_class = rol_serializer

class integrante_viewset(viewsets.ModelViewSet):
	queryset = Integrante.objects.all()
	serializer_class = integrante_serializer

class nacionalidad_viewset(viewsets.ModelViewSet):
	queryset = Nacionalidad.objects.all()
	serializer_class = nacionalidad_serializer
