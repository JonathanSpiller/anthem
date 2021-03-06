from monitor.models import ActionType

# NB: Assumption made that the patient can only enter PRO once per day.

def pro_increase(actions):
    """Check for consecutively increasing PRO reports over 72 hours

    Args:
        actions (queryset): A list of actions for a patient

    Returns:
        Boolean: Rule triggered if there are 3 consecutively increasing PRO reports in the last 72 hours
    """
    _, actions_72 = actions

    PRO = ActionType.objects.get(name="PRO")

    PROs = [int(action.data) for action in actions_72 if action.action_type==PRO]
    
    if len(PROs) < 3:
        return False

    PROs = PROs[:3]
    if all(PRO_day > PRO_prev_day for PRO_day, PRO_prev_day in zip(PROs, PROs[1:])):
        return True
    return False