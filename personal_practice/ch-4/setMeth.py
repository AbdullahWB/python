set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Or set1.union(set2)
print(union_set) 

union = set1.union(set2)
print(union)

intersection_set = set1 & set2  # Or set1.intersection(set2)
print(intersection_set)

difference = set1.intersection(set2)
print(difference)

difference_set = set1 - set2  # Or set1.difference(set2)
print(difference_set) 

symmetric_diff_set = set1 ^ set2  # Or set1.symmetric_difference(set2)
print(symmetric_diff_set)