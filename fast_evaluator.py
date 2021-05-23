from evaluator import RANKS, SUITS, SortedRanks, Flush

FLUSH_SCORE = 5863

def ReadEvaluationTable():
    table = {}
    for line in open("evaluation_table.txt"):
        score, ranks = line.split()
        table[ranks] = int(score)
    return table

def EvaluateWithTable(cards, table):
    ranks = "".join([RANKS[r] for r in SortedRanks(cards)])
    score = table[ranks]
    return score + FLUSH_SCORE if Flush(cards) else score
