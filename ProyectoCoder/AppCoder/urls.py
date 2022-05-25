from django.urls import path
from AppCoder.views import cursor, profesores


urlpatterns = [
    path("cursor/", cursor),
    path("profesor", profesores),
]