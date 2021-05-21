# Utility Tools for Texas Hold'em Poker

1) **Simulator**: 
   
   A program that reads community and player cards from the file and estimates the winning probability for each player.
   
   Example usage: `python3 simulator.py example_cards.txt`
   
   Customise `example_cards.txt` file or pass your own file as a command-line argument.
   
2) **Evaluator**:

   A function that evaluates one hand.
   
   Example usage:
   
   ```
   from evaluator import Evaluate
   hand1 = ["3h", "3c", "Kc", "Jh", "Jd"]
   hand2 = ["Ts", "Td", "Ad", "Qs", "Qd"]
   hand3 = ["Th", "Ts", "Ah", "Qc", "Qh"]
   Evaluate(hand1) < Evaluate(hand2) # True
   Evaluate(hand2) == Evaluate(hand3) # True
   Evaluate(hand2) > Evaluate(hand3) # False
   ```
   
    If you want to know more info about the hand:
    ```
    from evaluator import COMBOS
    combo, tiebreaker = Evaluate(hand1)
    print(COMBOS[combo]) # "Two pairs"
    print(tiebreaker) # [9, 9, 1, 1, 12], 9 for jacks, 1 for threes, 12 for the single king.
    ```
