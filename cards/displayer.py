SYMBOLS = {"h": "\u2764\uFE0F ",
           "d": "\u2666\uFE0F ",
           "s": "\u26AA",
           "c": ".%"}


def card_string(card):
    rank = "10" if card[0] == "T" else card[0]
    return rank + SYMBOLS[card[1]]


def display_row(row_name, row):
    formatted_row = [entry.ljust(10) for entry in row]
    print(f"{row_name}:".ljust(10) + ' '.join(formatted_row))


def display_cards(name, cards):
    string = name + ": " + '  '.join([card_string(card) for card in cards])
    print(string)
