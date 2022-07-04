from os.path import dirname
from evaluator import RANKS, SortedRanks, check_flush

FLUSH_SCORE = 5863


def read_evaluation_table():
    table_path = dirname(__file__) + "/evaluation_table.txt"
    rows = [row.split() for row in open(table_path)]
    return {row[1]: int(row[0]) for row in rows}


def evaluate_with_table(cards, table):
    ranks = "".join([RANKS[rank] for rank in SortedRanks(cards)])
    score = table[ranks]
    return score + FLUSH_SCORE if check_flush(cards) else score
