# Several tools for Texas Hold'em Poker

1) **Play**:

    A program that you can customize to play against computer opponents

    Example usage: `python3 play.py`

    Customize `play.py` to set different opponents

2) **Analyze**: 
   
   A program that reads community and player cards from the file and estimates the winning probability for each player.
   
   Example usage: `python3 analyze.py example_cards.txt`
   
   Customise `example_cards.txt` file or pass your own file as a command-line argument.
   
3) **Evaluator**:

   A function that evaluates one hand.
   
   Example usage:
   
   ```
   from cards.evaluator import evaluate
   hand1 = ["3h", "3c", "Kc", "Jh", "Jd"]
   hand2 = ["Ts", "Td", "Ad", "Qs", "Qd"]
   hand3 = ["Th", "Ts", "Ah", "Qc", "Qh"]
   evaluate(hand1) < evaluate(hand2) # True
   evaluate(hand2) == evaluate(hand3) # True
   evaluate(hand2) > evaluate(hand3) # False
   ```
   
    If you want to know more info about the hand:
    ```
    from cards.evaluator import COMBOS
    combo, tiebreaker = evaluate(hand1)
    print(COMBOS[combo]) # "Two pairs"
    print(tiebreaker) # [9, 9, 1, 1, 12], 9 for jacks, 1 for threes, 12 for the single king.
    ```
