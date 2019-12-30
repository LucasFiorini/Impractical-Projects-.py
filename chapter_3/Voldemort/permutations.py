from itertools import permutations

name = 'lucas'
permutation = [''.join(i) for i in permutations(name)]
print(len(permutation))
print(permutation)