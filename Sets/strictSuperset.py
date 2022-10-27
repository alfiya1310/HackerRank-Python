def isstrictsuperset(a,b):
    return b.issubset(a) and not(a.issubset(b))

a = set(int(x) for x in input().split(' '))
n = int(input())
result = True

for _ in range(n):
    b = set(int(x) 
    for x in input().split(' '))
    result &= isstrictsuperset(a,b)
    
print(result)
