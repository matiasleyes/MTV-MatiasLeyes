from django.urls import path
from AppCoder.views import cursor, profesores
from AppCoder.views import mi_plantilla


urlpatterns = [
    path("cursor/", cursor),
    path("profesor", profesores),
    path("mi_plantilla", mi_plantilla),
]