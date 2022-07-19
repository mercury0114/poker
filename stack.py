FULL_STACK = 200


def compute_pot(old_stack, new_stack):
    return sum(old - new for old, new in zip(old_stack, new_stack))


def full_stack_for_all(number_of_players):
    return [FULL_STACK] * number_of_players


def valid_stack(stack):
    return 1 < len(stack) <= 10 and all(s >= 2 for s in stack)
