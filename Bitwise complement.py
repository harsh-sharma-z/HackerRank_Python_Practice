arr=list(map(int,input().split()))
ans = 0
for i in arr:
    ans=ans+(~i)
    
ans=str(ans)
lst=[]
lst[:0]=ans

if(lst.count('0')>0):
    print("YES")
else:
    print("NO")
    
 
