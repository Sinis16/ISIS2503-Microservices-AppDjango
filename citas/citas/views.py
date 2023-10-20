from .models import Cita
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_paciente(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    pacientes = r.json()
    for paciente in pacientes:
        if data["paciente"] == paciente["id"]:
            return True
    return False

def CitaList(request):
    queryset = Cita.objects.all()
    context = list(queryset.values('id', 'paciente', 'fecha', 'hora_inicio', 'hora_fin', 'estado', 'dateTime'))
    return JsonResponse(context, safe=False)

def CitaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_paciente(data_json) == True:
            cita = Cita()
            cita.paciente = data_json['paciente']
            cita.fecha = data_json['fecha']
            cita.hora_inicio = data_json['hora_inicio']
            cita.hora_fin = data_json['hora_fin']
            cita.estado = data_json['estado']
            cita.save()
            return HttpResponse("successfully created cita")
        else:
            return HttpResponse("unsuccessfully created cita. Paciente does not exist")

def CitasCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        cita_list = []
        for cita in data_json:
                    if check_paciente(cita) == True:
                        db_cita = Cita()
                        db_cita.paciente= cita['paciente']
                        db_cita.fecha = cita['fecha']
                        db_cita.hora_inicio = cita['hora_inicio']
                        db_cita.hora_fin = cita['hora_fin']
                        db_cita.estado = cita['estado']
                        cita_list.append(db_cita)
                    else:
                        return HttpResponse("unsuccessfully created cita. Paciente does not exist")
        
        Cita.objects.bulk_create(cita_list)
        return HttpResponse("successfully created measurements")