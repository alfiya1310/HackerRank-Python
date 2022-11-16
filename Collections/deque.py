from collections import deque

d = deque()

for _ in range(int(input())):
    N = input().split()
    getattr(d, N[0])(*[N[1]] if len(N) > 1 else [])
    
print(*[item for item in d])