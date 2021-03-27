from monitor.models import ActionType

def no_med_report(actions):
    
    _, actions_72 = actions

    medication = ActionType.objects.get(name="Medication")

    medication_actions = [action for action in actions_72 if action.action_type==medication]

    if len(medication_actions) < 3:
        return True
    return False

# Assumption made that the patient can only enter medication once per day.