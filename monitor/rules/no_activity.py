def no_activity(actions):
    """Counts patient actions over last 24 hours

    Args:
        actions (queryset): A list of actions for a patient

    Returns:
        Boolean: Rule triggered if there are no actions in the last 24 hours
    """
    actions_24, _ = actions

    if not actions_24:
        return True
    return False