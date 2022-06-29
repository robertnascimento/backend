"""PrimeiroSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, contato, mecax, marcas,caduser,vendercarro,login,veiculo

urlpatterns = [ #As urls são colocadas aqui, com 2 parametros, o nome da url e a viw que o usuario vai acessar
  #  path ('inicio', home),
    path ('marcas/', marcas),
    path ('admin/', admin.site.urls),
    path ('templates/meca/',mecax),
    path ('login/',login),
    path ('veiculos.html',veiculo),
    path ('vendercarro/',vendercarro),
    path ('caduser/',caduser, name='caduser'),
    #nome é na URL     como esta em views
    path ('contato/', contato, name='contato'),
    path ('home/', home), #Não tem nada entre as aspas pois essa sera a pagina inicial, acessado por "localhoste:8000"
]
