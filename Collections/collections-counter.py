import collections

X = int(input())
shoes = collections.Counter(map(int, input().split()))
N = int(input())

income = 0

for i in range(N):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(income)