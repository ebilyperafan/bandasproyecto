from django.urls import path, include
from rest_framework import routers
from bandas.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'bandas', banda_viewset)
router.register(r'roles', rol_viewset)
router.register(r'integrantes', integrante_viewset)
router.register(r'nacionalidades', nacionalidad_viewset)

urlpatterns = [
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]