n = int(input())
s = set(map(int, input().split()))
operations = int(input())

for x in range(operations):
  operation = input().split()
  if operation[0] == "remove":
    s.remove(int(operation[1]))
  elif operation[0] == "discard":
    s.discard(int(operation[1]))
  else:
    s.pop()
    
print(sum(s))