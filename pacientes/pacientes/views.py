from .models import Paciente
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def PacienteList(request):
    queryset = Paciente.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def PacienteCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        paciente = Paciente()
        paciente.name = data_json["name"]
        paciente.save()
        return HttpResponse("successfully created variable")