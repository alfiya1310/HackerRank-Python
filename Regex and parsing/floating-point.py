import re

for _ in range(int(input())):
    N = input()
    pattern = '^[-+]?[0-9]*\.[0-9]+$'
    result = re.match(pattern,N)

    if result:
        print(True)
    else:
        print(False)