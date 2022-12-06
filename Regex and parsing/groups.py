import re

S = re.findall(r"([A-Za-z0-9])\1+",input())
if S:
    print(S[0])
else:
    print(-1)