FULL_STACK = 200


def full_stack_for_all(number_of_players):
    return [FULL_STACK] * number_of_players


def valid_stack(stack):
    return 1 < len(stack) <= 10 and all(s > 1 for s in stack)
