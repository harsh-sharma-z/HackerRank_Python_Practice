n,m=map(int,input().split())
num=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=set(l1)
b=set(l2)

tot=0

for i in num:
    if(i in a):
        tot=tot+1
    elif(i in b):
        tot=tot-1
