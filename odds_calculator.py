INFINITY = "inf"


def similar_odds(number, another_number):
    if INFINITY in [number, another_number]:
        return number == another_number
    return abs(float(number) - another_number) <= 0.05 * another_number


def loosing_odds(win_count, player):
    if win_count[player] == 0:
        return INFINITY
    return (sum(win_count.values()) - win_count[player]) / win_count[player]
