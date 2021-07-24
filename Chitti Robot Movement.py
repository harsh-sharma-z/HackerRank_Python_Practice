s=input()
lst=list(s)
k=0
for i in lst:
    if (i=='U' or i=='R'):
        k=k+1
    else:
        k=k-1
        
if(k==0):
    print("true")
else:
    print("false")
