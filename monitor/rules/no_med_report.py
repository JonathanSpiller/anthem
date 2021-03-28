from monitor.models import ActionType

# NB: Assumption made that the patient can only enter medication once per day.

def no_med_report(actions):
    """Counts medication report actions over last 72 hours

    Args:
        actions (queryset): A list of actions for a patient

    Returns:
        Boolean: Rule triggered if there are fewer than 3 medication reports in the last 72 hours
    """
    _, actions_72 = actions

    medication = ActionType.objects.get(name="Medication")

    medication_actions = [action for action in actions_72 if action.action_type==medication]

    if len(medication_actions) < 3:
        return True
    return False