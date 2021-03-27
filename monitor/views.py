from django.shortcuts import render, redirect
from .models import Patient, Alert, Setting
from datetime import timezone


def alerts(request):
    patients = Patient.objects.all()
    data = []

    for patient in patients:
        data.append({
            'patient': patient, 
            'alerts': Alert.objects.filter(patient=patient).order_by('time')
        })

    return render(request, 'alerts.html', {'data': data})


def critical(request):
    patients = Patient.objects.all()
    data = []

    for patient in patients:
        data.append({
            'patient': patient, 
            'alerts': Alert.objects.filter(patient=patient, alert_type='danger').order_by('time')
        })

    return render(request, 'alerts.html', {'data': data})


def patient(request, id):
    patient = Patient.objects.get(id=id)
    data = []

    data.append({
        'patient': patient, 
        'alerts': Alert.objects.filter(patient=patient).order_by('time')
    })

    return render(request, 'alerts.html', {'data': data})


def clear(request):
    Alert.objects.all().delete()
    return redirect('alerts')