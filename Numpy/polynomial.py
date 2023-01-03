import numpy

P = list(map(float,input().split()))
x = input()

print(numpy.polyval(P,int(x)))