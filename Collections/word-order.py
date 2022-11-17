from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

n = OrderedCounter(input() for _ in range(int(input())))

print(len(n))
print(*n.values())