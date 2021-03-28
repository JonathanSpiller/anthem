import threading
from .models import *
from cprint import cprint
from datetime import datetime, timedelta
from django.utils import timezone

"""
  To Add New Rules
  1. Add the rule file to the rules folder
  2. Import the file (below)
  3. Update the dispatcher with the correct function name (below)
  4. Add the rule to the database to activate it (Admin panel)
"""
from .rules.no_activity import no_activity
from .rules.five_done import five_done
from .rules.no_med_report import no_med_report
from .rules.pro_increase import pro_increase

dispatcher = {
    'no_activity': no_activity,
    'no_med_report': no_med_report,
    'five_done': five_done,
    'pro_increase': pro_increase
}


def _get_monitor_settings():
    """Fetches monitor_active flag and monitor timing (in seconds) from the database

    Args:
        None

    Returns:
        Tuple: A tuple containing a monitor_active flag and monitor time
    """
    settings = Setting.objects.get(id=1)
    return settings.monitor, settings.monitor_time


def _get_patients():
    """Fetches a queryset of all patients

    Args:
        None

    Returns:
        List: A queryset containing all Patient objects
    """
    return Patient.objects.all()


def _get_rules():
    """Fetches a queryset of all patients

    Args:
        None

    Returns:
        List: A queryset containing all Rule objects ordered by priority
    """
    return Rule.objects.all().order_by('priority')


def _get_actions(patient):
    """Fetches a queryset of all actions per patient over the last 24 and 72 hours

    Args:
        patient (Patient): A Patient Object

    Returns:
        Tuple: A tuple containing querysets of patient actions over the last 24 and 72 hours
    """
    hr_24 = timezone.now() - timedelta(days=1)
    hr_72 = timezone.now() - timedelta(days=3)

    actions_24 = Action.objects.filter(patient=patient, time__gte=hr_24).order_by('-time')
    actions_72 = Action.objects.filter(patient=patient, time__gte=hr_72).order_by('-time')

    return (actions_24, actions_72)


def check_database():
    """Runs all rules for each patient.
    For each rule that is triggered, an alert is written to the Alerts Table

    Args:
        None

    Returns:
        None
    """
    cprint.info("[CHECKING DATABASE]")
    
    rules = _get_rules()
    patients = _get_patients()

    for patient in patients:
        cprint.ok(patient)
        actions = _get_actions(patient)

        cprint.warn('    Checking Rules...')
        for rule in rules:
            function_name = rule.function_name
            alert = dispatcher[function_name](actions)
            if alert:
                Alert.objects.create(patient=patient, message=rule.alert_message, alert_type=rule.alert_type)
            
            cprint.warn('       ',rule.function_name, '-', alert)


def run_monitor():
    """Runs activity monitoring every X minutes.
    Thread timer X is read from the database and a background thread is set to execute after X minutes.

    Args:
        None

    Returns:
        None
    """
    monitor_active, monitor_time = _get_monitor_settings()
    threading.Timer(monitor_time, run_monitor).start()
    cprint.ok(f"[MONITOR INTERVAL] {monitor_time} seconds")
    if monitor_active:
        cprint.info("[MONITOR ACTIVE]")
        check_database()
    else:
        cprint.warn("[MONITOR INACTIVE]")