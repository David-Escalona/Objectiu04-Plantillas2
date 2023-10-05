"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Proyecto1.views import saludo, despedida, dameFecha, calculaEdad, pagina1, pagina2, pagina3, info, nombreyedad, habitant

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('habitant/', habitant),
    path('adios/', despedida),
    path('fecha/', dameFecha),
    path('edades/<int:edad>/<int:agno>', calculaEdad),
    path('p1/', pagina1),
    path('p2/', pagina2),
    path('p3/', pagina3),
    path('info/', info),
    path('nombreyedad/<nombre>/<int:agno>', nombreyedad)
]
