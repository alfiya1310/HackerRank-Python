import numpy

n,m = map(int,input().split())

list1 = [list(map(int,input().split())) for i in range(n)]

array_1 = numpy.array(list1)

print(max(numpy.min(array_1,axis=1)))