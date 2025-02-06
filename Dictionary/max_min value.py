scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
h_scorer = max(scores, key=scores.get)
l_scorer = min(scores, key=scores.get)
print("Highest Scorer:", h_scorer, "->", scores[h_scorer])
print("Lowest Scorer:", l_scorer, "->", scores[l_scorer])