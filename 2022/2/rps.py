shape_scores = {"X": 0,"Y": 1, "Z": 3}
outcome_scores = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

total_score = 0
filepath = "input.txt"

with open(filepath, "r") as f:
    for line in f:
        line = line.strip()
        total_score += outcome_scores[line]

print(total_score)
