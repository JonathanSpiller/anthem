from django.urls import path
from . import views

urlpatterns = [
    path('', views.alerts, name='alerts'),
    path('patient/<int:id>', views.patient, name='patient'),
    path('critical/', views.critical, name='critical'),
    path('clear/', views.clear, name='clear'),
]
