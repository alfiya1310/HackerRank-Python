if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = map(int, input().split())
    arr=sorted(arr)
    arr2=[]
    for i in arr:
        if i not  in arr2:
            arr2.append(i)
    print(arr2[-2])
                