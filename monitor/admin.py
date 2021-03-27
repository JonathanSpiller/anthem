from django.contrib import admin
from .models import *
# Register your models here.


class RuleAdmin(admin.ModelAdmin):
    list_display = ('text', 'alert_message', 'priority')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'program')

class ActionAdmin(admin.ModelAdmin):
    list_display = ('time', 'patient', 'action_type', 'data')
    readonly_fields = ('time',)

class AlertAdmin(admin.ModelAdmin):
    list_display = ('time', 'patient', 'message')

admin.site.register(Action, ActionAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Rule, RuleAdmin)

admin.site.register(Program)
admin.site.register(ActionType)
admin.site.register(Setting)