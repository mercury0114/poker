from evaluator import RANKS, SUITS, SortedRanks, Flush

FLUSH_SCORE = 5863

def ReadEvaluationTable():
    table_file = open("evaluation_table.txt")
    table = {}
    for line in table_file:
        rank, hand = line.split()
        table[hand] = int(rank)
    table_file.close()
    return table

def EvaluateWithTable(cards, table):
    ranks = SortedRanks(cards)
    string = "".join([RANKS[r] for r in ranks])
    score = table[string]
    return score + FLUSH_SCORE if Flush(cards) else score
