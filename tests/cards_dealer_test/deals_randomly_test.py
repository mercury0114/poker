from sys import path
path.append("../../")

from cards_dealer import deal_cards

for _ in range(100):
    assert deal_cards() != deal_cards()

print("deals_randomly_test.py passed")
