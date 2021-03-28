def five_done(actions):
    """Counts patient actions over last 24 hours

    Args:
        actions (queryset): A list of actions for a patient

    Returns:
        Boolean: Rule triggered if there are 5 or more actions in the last 24 hours
    """
    actions_24, _ = actions

    if len(actions_24) >= 5:
        return True
    return False