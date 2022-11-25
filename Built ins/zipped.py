N, X = map(int, input().split()) 

score = []
for _ in range(X):
    score.append( map(float, input().split()) ) 

for i in zip(*score): 
    print(sum(i) / len(i))