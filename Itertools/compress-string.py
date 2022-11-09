from itertools import groupby

for X, c in groupby(input()):
   print('({}, {})'.format(len(list(c)), X), end=" ")