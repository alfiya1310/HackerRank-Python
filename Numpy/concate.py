import numpy as np

array_1, array_2, array_3 = map(int,input().split())

arrayA = np.array([input().split() for _ in range(array_1)],int)
arrayB = np.array([input().split() for _ in range(array_2)],int)

print(np.concatenate((arrayA, arrayB), axis = 0))