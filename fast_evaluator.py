from evaluator import RANKS, SUITS, SortedRanks, Flush

FLUSH_SCORE = 5863

def ReadEvaluationTable():
    return {row.split()[1] : int(row.split()[0]) for row in open("evaluation_table.txt")}

def EvaluateWithTable(cards, table):
    ranks = "".join([RANKS[rank] for rank in SortedRanks(cards)])
    score = table[ranks]
    return score + FLUSH_SCORE if Flush(cards) else score
