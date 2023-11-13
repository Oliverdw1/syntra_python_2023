pairs = [(1, 2), (3, 3), (2, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1] - x[0])
print(sorted_pairs)