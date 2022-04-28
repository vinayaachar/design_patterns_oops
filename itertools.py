from itertools import permutations, combinations, accumulate, groupby
import operator


a = [1, 2, 3, 4, 5]

perm = permutations(a, 2)
comb = combinations(a, 2)
acc = accumulate(a, func=operator.mul)

# print('permutations', list(perm))
# print('combination', list(comb))

# print('accumulate', list(acc))
group = groupby(a, lambda x: x < 3)


for k, v in group:
    print(k, list(v))

d = dict()
d['first'].add('vinay')
print(d.get('first'))
