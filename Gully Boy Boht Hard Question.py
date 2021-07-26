s=input()
n= int(input())
t=int(input())
st=""
for i in range ((n),len(s)):
    if(s[i]==" "):
        st=st+""
    else:
        st=st+s[i]
        st=st+" "
        
    
    
for i in range (0,n):
    if(s[i]==" "):
        st=st+""
    else:
        st=st+s[i]
        st=st+" "
    
for i in range (t):
    print(st,end="")
