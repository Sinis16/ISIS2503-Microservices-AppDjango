from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^citas/', views.CitaList),
    url(r'^citacreate/$', csrf_exempt(views.CitaCreate), name='citaCreate'),
    url(r'^createcitas/$', csrf_exempt(views.CitasCreate), name='createCitas'),
]