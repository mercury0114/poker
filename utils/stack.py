FULL_STACK = 200


def compute_pot(old_stack, new_stack):
    return sum(old - new for old, new in zip(old_stack, new_stack))


def split_pot(old_stack, stack, ranks):
    rank = 0
    splits = [0] * len(stack)
    while stack != old_stack:
        for i, _ in enumerate(ranks):
            if old_stack[i] == stack[i]:
                ranks[i] = len(ranks)
        if not sum(old_stack[i] - stack[i] for i in range(len(stack)) if ranks[i] == rank):
            rank += 1
            continue
        min_investment = min(
            old - new for old, new in zip(old_stack, stack) if old - new != 0)
        pot = sum(min(old - new, min_investment)
                  for old, new in zip(old_stack, stack))
        for i, _ in enumerate(stack):
            bonus = min(min_investment, old_stack[i] - stack[i])
            stack[i] += bonus
            if ranks[i] == rank and bonus:
                splits[i] += pot // ranks.count(rank)
    return splits


def full_stack_for_all(number_of_players):
    return [FULL_STACK] * number_of_players


def valid_stack(stack):
    return 1 < len(stack) <= 10 and all(s >= 2 for s in stack)
