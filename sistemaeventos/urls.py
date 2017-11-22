"""sistemaeventos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from backend.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuario', UserViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'cidade', CidadeViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'pessoa', PessoaViewSet)
router.register(r'pessoafisica', PessoaFisicaViewSet)
router.register(r'evento', EventoViewSet)
router.register(r'ticket', TicketViewSet)
router.register(r'inscricao', InscricaoViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
