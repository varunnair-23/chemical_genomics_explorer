#define list of scores
scores = [91.5, 72.0, 88.5, 64.8, 99.0, 55.5]

#define list of winning scores
winning_scores = [score for score in scores if score >= 70]

#print the scores, and print the winning scores
print("All scores:", scores)
print("Winning scores:", winning_scores)

player_scores = {
    "John": [90, 85, 88],
    "Ben": [78, 82, 86],
    "Alice": [92, 88, 91]
}

for name, totals in player_scores.items():
    average = sum(totals) / len(totals)
    print(f"{name}'s average score: {average:.2f}")