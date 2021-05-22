from evaluator import RANKS, SUITS, SortedRanks, Flush

FLUSH_SCORE = 5863

def ReadEvaluationTable():
    table_file = open("evaluation_table.txt")
    table = {}
    for line in table_file:
        score, ranks = line.split()
        table[ranks] = int(score)
    table_file.close()
    return table

def EvaluateWithTable(cards, table):
    ranks = "".join([RANKS[r] for r in SortedRanks(cards)])
    score = table[ranks]
    return score + FLUSH_SCORE if Flush(cards) else score
