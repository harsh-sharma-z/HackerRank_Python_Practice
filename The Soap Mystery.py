n=int(input())
arr=list(map(int,input().split()))
q=int(input())
for i in range (q):
    k=int(input())
    c=0
    for j in arr:
        if(j<k):
            c+=1
    print(c)
