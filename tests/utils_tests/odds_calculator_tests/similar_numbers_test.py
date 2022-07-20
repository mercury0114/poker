from sys import path
path[0] = "../../../"

from utils.odds_calculator import similar_odds

assert similar_odds(3, 3.05)
assert similar_odds(0, 0)
assert similar_odds(0.0999, 0.1)
assert similar_odds(2, 2.1)
assert similar_odds("inf", "inf")
assert not similar_odds(1000, "inf")
assert not similar_odds(1, 1.1)
print("Passed")
