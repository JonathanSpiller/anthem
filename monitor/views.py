from django.shortcuts import render, redirect
from .models import Patient, Alert, Setting
from datetime import timezone


def alerts(request):
    """Renders the alerts page showing ALL alerts
    """
    patients = Patient.objects.all()
    data = []

    for patient in patients:
        data.append({
            'patient': patient, 
            'alerts': Alert.objects.filter(patient=patient).order_by('time')
        })

    return render(request, 'alerts.html', {'data': data})


def critical(request):
    """Renders the alerts page showing ONLY CRITICAL alerts
    """
    patients = Patient.objects.all()
    data = []

    for patient in patients:
        data.append({
            'patient': patient, 
            'alerts': Alert.objects.filter(patient=patient, alert_type='danger').order_by('time')
        })

    return render(request, 'alerts.html', {'data': data})


def patient(request, id):
    """Renders the alerts page showing alerts for a particular patient
    """
    patient = Patient.objects.get(id=id)
    data = []

    data.append({
        'patient': patient, 
        'alerts': Alert.objects.filter(patient=patient).order_by('time')
    })

    return render(request, 'alerts.html', {'data': data})


def clear(request):
    """Deletes all alerts from the database
    """
    Alert.objects.all().delete()
    return redirect('alerts')