n = int(input())
l1 = list(input().split())
m = int(input())
l2 = list(input().split())

s1 = set(l1)
s2 = set(l2)

print(len(s1.union(s2)))